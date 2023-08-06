#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>

#define MAX_INODES 1024
#define BAD_INODE_NUM 1025

typedef struct Inode {
	uint32_t name;
	uint8_t file_type; 
} Inode;

typedef struct InodeName { 
	uint32_t name;
	char file_name[33]; // needs to be null terminated before you can string compare
}
InodeName;
Inode* getInode (Inode inodes_list[], int length, uint32_t inode_name);
int readInodeNames(InodeName inode_names[], Inode* curr_dir);
uint32_t getInodeFromFileName (InodeName inode_names[], int length, char* inode_file_name);
void writeInodeNames(InodeName inode_names[], int length, Inode* curr_dir);
char *uint32_to_str(uint32_t i);

int main (int argc, char *argv[]) {
	if (argc != 2) {
		printf("You must have one parameter which is the directory containing the file system.");
		exit(0);
	}
	if (chdir(argv[1]) != 0) {
		printf("Cannot enter directory.");
		exit(0);
	}

	Inode inodes_list[1024] = {0}; // was set to 0's but changed 
	InodeName inode_names[1024] = {0}; // was set to 0's but changed 
	int inode_names_counter = 0;

	int inodes_counter = 0;
	FILE *inode_file = fopen("inodes_list", "rb");
	while (1) {
		size_t bytes_read = fread(&inodes_list[inodes_counter], 5, 1, inode_file);		
		if (bytes_read == 0) {
			break;
		}
		inodes_counter++;
	}	

	fclose(inode_file);
	// printf("%d", inodes_counter);
	
	
	for (int i = 0; i < inodes_counter; i++) {
		if (inodes_list[i].name >= MAX_INODES) {
			printf("Inode numbers outside of range:%ud\n", inodes_list[i].name);
		}
		if (inodes_list[i].file_type != 'd' && inodes_list[i].file_type != 'f') {
		       printf("Invalid file type indicator: %c\n", inodes_list[i].file_type);
		}
		
	}

	Inode *curr_dir = getInode(inodes_list, inodes_counter, 0);
	if (curr_dir == NULL) {
		printf("Inode 0 does not exist.");		
		exit(0);
	}
	if (curr_dir -> file_type != 'd') {
		printf("Root is not a directory.");
		exit(0);
	}

	
	inode_names_counter = readInodeNames(inode_names, curr_dir);
	uint32_t parent_dir = getInodeFromFileName(inode_names, inode_names_counter, "..");
	while(1) {
		printf("> ");
		char command[513];
		if (fgets(command, 513, stdin) == NULL) {
			break;
		}
		

		char *token;
		token = strtok(command, "\n ");

		if (token == NULL) {
			continue;
		}
		
	
		if (strcmp(token, "exit") == 0) {
			break;
		} else if (strcmp(token, "mkdir") == 0) {
			char *dir = strtok(NULL, "\n ");
			if (dir == NULL) {
				printf("Specify a directory to make.");
				continue;
			}
			uint32_t next_dir_name = getInodeFromFileName(inode_names, inode_names_counter, dir);
			if (next_dir_name != BAD_INODE_NUM) {
				printf("This file already exists.");
				continue;
			} 
			// create a new inode with the next available inode number
			// add this inode to the current directory as a directory
			// create a file for writing
			// write two inode name structs, one for . (new inode number), one for .. (parent of new 				folder which is the current folder)
			if (inodes_counter == MAX_INODES) {
				printf("No more inodes available.");
				continue;
			}
			//  might cause errors if we need to delete inodes 
			uint32_t next_inode = inodes_counter;
			Inode inode = {.name = next_inode, .file_type = 'd'};
			inodes_list[inodes_counter] = inode;
			inodes_counter++;
			InodeName inode_name = {};
			inode_name.name = next_inode;
			strncpy(inode_name.file_name, dir, 32);

			inode_names[inode_names_counter] = inode_name;
			inode_names_counter++;
			writeInodeNames(inode_names, inode_names_counter, curr_dir);
			InodeName new_dir_entries[2] = {0};
			new_dir_entries[0].name = next_inode;
			strcpy(new_dir_entries[0].file_name, ".");
			new_dir_entries[1].name = curr_dir->name;
                        strcpy(new_dir_entries[1].file_name, "..");
			writeInodeNames(new_dir_entries, 2, &inode);

		} else if (strcmp(token, "cd") == 0) {
			// check if the directory we want to cd into exists
			// if it does not exist print a message and don't do anything
			char* dir = strtok(NULL, "\n ");
			if (dir == NULL) {
				printf("Specify a directory to cd into.");
				continue;
			}
			uint32_t next_dir_name = getInodeFromFileName(inode_names, inode_names_counter, dir); 
			if (next_dir_name == BAD_INODE_NUM) {
				printf("This directory does not exist.\n");
				continue;
			}
			Inode* next_dir = getInode(inodes_list, inodes_counter, next_dir_name);
			// check if next_dir is a directory or a file
			if (next_dir->file_type != 'd') {
				printf("This is not a directory.\n");
				continue;
			}
			curr_dir = next_dir;
			inode_names_counter = readInodeNames(inode_names, curr_dir);
			parent_dir = getInodeFromFileName(inode_names, inode_names_counter, "..");
		} else if (strcmp(token, "ls") == 0) {
			for (int i = 0; i < inode_names_counter; i++) {
				char file_name[33] = {0};
				strncpy(file_name, inode_names[i].file_name, 32);
				printf("%u %s\n", inode_names[i].name, file_name); 
			}
			
		} else if (strcmp(token, "touch") == 0) {
			char *file = strtok(NULL, "\n ");
                        if (file == NULL) {
                                printf("Specify a file to make.");
                                continue;
                        }
                        uint32_t next_file_name = getInodeFromFileName(inode_names, inode_names_counter, file);
                        if (next_file_name != BAD_INODE_NUM) {
                                continue;
                        }
                       
                        if (inodes_counter == MAX_INODES) {
                                printf("No more inodes available.");
                                continue;
                        }
                        // this is naive, might cause errors if we need to delete inodes 
                        uint32_t next_inode = inodes_counter;
                        Inode inode = {.name = next_inode, .file_type = 'f'};
                        inodes_list[inodes_counter] = inode;
                        inodes_counter++;
                        InodeName inode_name = {};
                        inode_name.name = next_inode;
                        strncpy(inode_name.file_name, file, 32);

                        inode_names[inode_names_counter] = inode_name;
                        inode_names_counter++;
                        writeInodeNames(inode_names, inode_names_counter, curr_dir);
                        char *inode_file_name = uint32_to_str(next_inode);
		
			FILE *new_file = fopen(inode_file_name, "w");
			free(inode_file_name);
			fprintf(new_file, "%s\n", file);
			fclose(new_file);
		
		} else {
			printf("Invalid command.\n");
		}
	}
		
	// requirement 5
	inode_file = fopen("inodes_list", "wb");
	
	for (int i = 0; i < inodes_counter; i++) {
		fwrite(&inodes_list[i], 5, 1, inode_file);
	}
	fclose(inode_file);
}

Inode* getInode (Inode inodes_list[], int length, uint32_t inode_name) {
	// make sure inode name is in inodes_list
	for (int i = 0; i < length; i++) {
		if (inodes_list[i].name == inode_name) { 
			return &inodes_list[i];
		}
	}
	return NULL;
}

uint32_t getInodeFromFileName (InodeName inode_names[], int length, char* inode_file_name) {
        for (int i = 0; i < length; i++) {
                if (strncmp(inode_names[i].file_name, inode_file_name, 32) == 0) {
                        return inode_names[i].name;
                }
        }
        return BAD_INODE_NUM;
}

char *uint32_to_str(uint32_t i) {
   int length = snprintf(NULL, 0, "%lu", (unsigned long)i);       // pretend to print to a string to determine length
   char* str = malloc(length + 1);                        // allocate space for the actual string
   snprintf(str, length + 1, "%lu", (unsigned long)i);            // print to string

   return str;
}

int readInodeNames(InodeName inode_names[], Inode* curr_dir) {
	int inodes_counter = 0;
	char *inode_file_name = uint32_to_str(curr_dir -> name);

        FILE *file = fopen(inode_file_name, "rb");
	free(inode_file_name);
	while (1) {
                size_t bytes_read = fread(&inode_names[inodes_counter], 36, 1, file);
                if (bytes_read == 0) {
                        break;
                }
                inodes_counter++;
        }

        fclose(file);
	return inodes_counter; // returning how many names are in the directory
}

void writeInodeNames(InodeName inode_names[], int length, Inode* curr_dir) {
	char *inode_file_name = uint32_to_str(curr_dir -> name);
	
	FILE *file = fopen(inode_file_name, "wb");
	free(inode_file_name);
	for (int i = 0; i < length; i++) {
		fwrite(&inode_names[i], 36, 1, file);
	}
	fclose(file);
}
