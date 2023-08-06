#include <sys/stat.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "hash.h"
#include <signal.h>

Hash* hash;
FILE *named_pipe;

void cleanup(int signum) {
	destroyHash(hash);
	if (named_pipe != NULL) {
		fclose(named_pipe);
	}
	exit(0);
}

int main(int argc, char *argv[]) {
	if (argc != 3) {
		printf("Needs to be 3 command line arguments.");
		exit(-1);
	}
	FILE *db_file = fopen(argv[1], "r");
	hash = makeHash();
	//cleanup(0);
	char buffer[1100];
	long int offset_counter = 0;
	if (db_file != NULL) {	
		while (fgets(buffer, 1058, db_file)) {
			int i = 0;
			while (buffer[i] != ',') {
				i++;
				continue;
			}
			buffer[i] = '\0';
			char key[33];
			strcpy(key, buffer);
			offset_counter += (1 + strlen(key));
			setHash(hash, key, offset_counter);
			offset_counter += strlen(buffer + 1 + strlen(key)); // length of value
		}
		fclose(db_file);
	} else {
		db_file = fopen(argv[1], "w");
		fclose(db_file);
	}
//	cleanup(0);
	struct stat statbuf;
	int res = stat(argv[2], &statbuf);
	if (res != 0) {
		//FIFO doesnt exist, creating the FIFO
		mkfifo(argv[2], 0600); // 6 means read write but no execution 
	} else if (!(S_ISFIFO(statbuf.st_mode))) {
		// this means it exists and it is a FIFO
		printf("This is not a FIFO.");
		exit(-1);
	}


	signal(SIGQUIT, cleanup);
	signal(SIGINT, cleanup); 

	while (1) {
		named_pipe = fopen(argv[2], "r");
		char key[33];
		char get_or_set[4];
		char value[1025];
		if (named_pipe == NULL) {
			printf("named_pipe is null");
			exit(-1);
		}
	
		if (fgets(buffer, 1100, named_pipe) == NULL) {
			fclose(named_pipe);
			named_pipe = NULL;
			continue;
		}
		fclose(named_pipe);
		named_pipe = NULL;
		//cleanup(0);

		sscanf(buffer, "%s %s %[^\n]", get_or_set, key, value);
		if (strcmp(get_or_set, "get") == 0) {
			char pipe_name_buffer[100];
			sprintf(pipe_name_buffer, "fifo_%s", key);
			mkfifo(pipe_name_buffer, 0600); 
			FILE *pipe_reading = fopen(pipe_name_buffer, "w");
			long int res = getHash(hash, value);
			if (res == -1) {
				fprintf(pipe_reading, "Key %s does not exist.", value);
			} else {
				char buffer_2[1100];
				db_file = fopen(argv[1], "r");
				fseek(db_file, res, SEEK_SET); // SEEK_SET is the start of the file
				fgets(buffer_2, 1100, db_file);
				int len = strlen(buffer_2);
				if (buffer_2[len - 1] == '\n') {
					buffer_2[len - 1] = '\0';
				}
				fprintf(pipe_reading, "%s\n", buffer_2);

				fclose(db_file);
			}
			fclose(pipe_reading);
		} else {
			db_file = fopen(argv[1], "r");	
			
			char temp_db_name[100] = "~";	
			strcat(temp_db_name, argv[1]);

			FILE *new_db_file = fopen(temp_db_name, "w");
		
			Node *linked_list = getAllKeys(hash);
			for (Node *node = linked_list; node != NULL; node = node->next) {
				if (strcmp(node->key, key) == 0) {
					continue;
				}
				long int offset = node->value;
				fseek(db_file, offset, SEEK_SET); 
                                char buffer_3[1100];
				fgets(buffer_3, 1100, db_file);
				int len_2 = strlen(buffer_3);
				if (buffer_3[len_2 - 1] == '\n') {
					buffer_3[len_2 - 1] = '\0';
				}
				fprintf(new_db_file, "%s,%s\n", node->key, buffer_3);
			}
			fclose(db_file);

			fprintf(new_db_file, "%s,%s\n", key, value);
			fclose(new_db_file);
			remove(argv[1]);
			rename(temp_db_name, argv[1]);
			
			Node *node = linked_list;
                	
			// clean up linked list here
			while (node != NULL) {
                                Node *temp_node = node;
                                node = node->next;
                                free(temp_node);
                        }
			destroyHash(hash);
			hash = makeHash();
			db_file = fopen(argv[1], "r");
	        	offset_counter = 0;
        		while (fgets(buffer, 1058, db_file)) {
               			int i = 0;
                		while (buffer[i] != ',') {
                        		i++;
                        		continue;
                		}
                		buffer[i] = '\0';
               			char key[33];
                		strcpy(key, buffer);
                		offset_counter += (1 + strlen(key));
                		setHash(hash, key, offset_counter);
               			offset_counter += strlen(buffer + 1 + strlen(key)); // length of value
        		}
        		fclose(db_file);
		}
	//	fclose(named_pipe);
	}
}
