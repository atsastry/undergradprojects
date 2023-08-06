#define _POSIX_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <stdint.h>
#include <netinet/in.h>
#include <sys/wait.h>
#include <sys/stat.h>

int socket_file_descriptor;
pid_t process_id;
pid_t kvstore_id;

void cleanup(int signum) {
	if (process_id > 0) {
		kill(process_id, SIGKILL);
		kill(kvstore_id, SIGQUIT);
	}
	shutdown(socket_file_descriptor, SHUT_RDWR); // shuts down tranmission and reception	
	exit(0);
}

void error_message(const char* num, const char* message, int accept_file_descriptor) {
	printf("HTTP/1.0 %s %s\r\n", num, message);
	char buffer[100];
	sprintf(buffer, "HTTP/1.0 %s %s\r\n", num, message);
	send(accept_file_descriptor, buffer, strlen(buffer), 0);
	close(accept_file_descriptor);
	exit(0);
}

int main(int argc, char *argv[]) {
	if (argc != 3) {
		printf("Only 2 command line arguments please.\n");
		exit(-1);
	}
	char *fifo_location = argv[1];
	kvstore_id = fork();
	if (kvstore_id == 0) {
		execlp("./kvstore", "./kvstore", "httpd.db", fifo_location, NULL);
		printf("kvstore failed to execute.");
		perror("kvstore failed.");
		exit(-1);
	}


	uint16_t port = atoi(argv[2]);

	if (port < 1024 || port > 65535) {
		printf("%d is not within the correct range of values", port);
		exit(-1);
	}
	socket_file_descriptor = socket(AF_INET, SOCK_STREAM, 0);

	if (socket_file_descriptor == -1) {
		printf("Unsuccessful socket creation.\n");
		exit(-1);
	}
	struct sockaddr_in addr;
	addr.sin_family = AF_INET;
	addr.sin_port = htons(port);
	addr.sin_addr.s_addr = INADDR_ANY;

	int bind_res = bind(socket_file_descriptor, (struct sockaddr*)&addr, sizeof(addr));

	if (bind_res == -1) {
		printf("New socket was not binded to the IP address. Error.\n");
		exit(-1);
	}
	int listen_res = listen(socket_file_descriptor, 1);

	if (listen_res == -1) {
		printf("Cannot accept request. Error.\n");
		exit(-1);
	}

	signal(SIGINT, cleanup);
	signal(SIGQUIT, cleanup);

	while (1){
		process_id = fork();
		if (process_id != 0) { // if it's a parent
			int stat_loc;
			waitpid(process_id, &stat_loc, 0);
			if (WEXITSTATUS(stat_loc) != 0) {
				printf("Exiting.\n");
				exit(-1);
			}
		} else { // if it's a child 
			int accept_file_descriptor = accept(socket_file_descriptor, NULL, NULL);
			if (accept_file_descriptor == -1) {
				printf("Accept failed\n");
				exit(0);
			}
			char buffer[1025] = {0};
			ssize_t bytes_read = recv(accept_file_descriptor, buffer, 1024, 0);
			// recv reads the bytes from the file that is referenced by the accept_file_descriptor
			// file descriptor is a number that represents an open (can put or receive) file

			if (bytes_read == 0) {
				printf("No messages available.\n");
				exit(-1);
			} 
			if (bytes_read == -1) {
				printf("Error retrieving messages.\n");
				exit(-1);
			}
			printf("%s\n", buffer);

			char *command_line = strtok(buffer, "\r\n");
//			printf("command line: %s\n", command_line);
			
			// make a new pointer and point it to the buffer after the command line
			char *buff_pointer = buffer + strlen(buffer) + 2;
			char *value;
			if (*buff_pointer == '\0') {
				value = NULL;
			}
			else if (strncmp(buff_pointer, "\r\n", 2) == 0) {
				value = buff_pointer + 2;
			} else {
				while (strncmp(buff_pointer, "\r\n\r\n", 4) != 0) {
					buff_pointer++;
				}
				value = buff_pointer + 4;
			}

			//char *other_line = strtok(NULL, "\r\n");

			//while (other_line != NULL && other_line[0] != '\0') {
			//	printf("Skipping%s\n", other_line);
			//	other_line = strtok(NULL, "\r\n");
				// NULL in strtok continues with original buffer
			//}
	
			//if (other_line != NULL) {
			//	value = strtok(NULL, "\r\n");
			//}

			char *first_command = strtok(command_line, " ");

			if (!(strcmp(first_command, "HEAD") == 0 || strcmp(first_command, "GET") == 0 || strcmp(first_command, "PUT") == 0))  {
				error_message("501", "Not Implemented", accept_file_descriptor);

			}

			char *file_name = strtok(NULL, " ");
			if (file_name == NULL) {	
				error_message("400", "Bad Request", accept_file_descriptor);
			}

			char curr_dir[1024] = ".";
			strcat(curr_dir, file_name); //file with a . in front of it 

			char header[1024] = {0};
			struct stat file_info = {0}; 
			int stat_res = stat(curr_dir, &file_info);

			// 400 cant parse 

			// prints header
			sprintf(header, "HTTP/1.0 200 OK\r\nContent-Type: text/html\r\nContent-Length: %ld\r\n\r\n", file_info.st_size);

			if (strcmp(first_command, "HEAD") == 0) {
				if (stat_res == -1) {
					error_message("404", "Not Found", accept_file_descriptor);
				}		
				send(accept_file_descriptor, header, strlen(header), 0);
			}

			else if (strcmp(first_command, "GET") == 0) {
				// load file, send file
				if (strncmp(file_name, "/kv/", 4) == 0) {
                                	pid_t process_id_2 = getpid();
					FILE *fifo_file = fopen(fifo_location, "w");
					char *key = file_name + 4;
					fprintf(fifo_file, "get %d %s", process_id_2, key);
					fclose(fifo_file);

					char fifo_name[1024];
                			sprintf(fifo_name, "fifo_%d", process_id_2);
					
					//printf("fifo name: %s\n", fifo_name);
					
					FILE *fifo_reading = fopen(fifo_name, "r");
					while (fifo_reading == NULL) {
						fifo_reading = fopen(fifo_name, "r");
					}

					char val[1024];
					fgets(val, 1024, fifo_reading);
					
					char key_DNE[2014];
					sprintf(key_DNE, "Key %s does not exist.", key);
					if (strcmp(val, key_DNE) == 0) {
						error_message("404", "Not Found", accept_file_descriptor);
					}

                			fclose(fifo_reading);
                			remove(fifo_name);
                			sprintf(header, "HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\nContent-Length: %ld\r\n\r\n", strlen(val));
					send(accept_file_descriptor, header, strlen(header), 0);
					send(accept_file_descriptor, val, strlen(val), 0);
					close(accept_file_descriptor);
					exit(0);
				}
				
				if (stat_res == -1) {
					error_message("404", "Not Found", accept_file_descriptor);
				}		
				void *data = malloc(file_info.st_size);

				if (data == NULL) {	
					error_message("500", "Internal Error", accept_file_descriptor);
				}
				send(accept_file_descriptor, header, strlen(header), 0);
				FILE *file = fopen(curr_dir, "r");
				fread(data, file_info.st_size, 1, file);
				send(accept_file_descriptor, data, file_info.st_size, 0);
				fclose(file);
				free(data);

					
		
			} else { //command is PUT
				if (strncmp(file_name, "/kv/", 4) != 0) {	
					error_message("403", "Permission Denied", accept_file_descriptor);		
				}
				char buffer_2[1024] = {0};
				if (value == NULL) { 
				//	fprintf(stderr, "value is null.\n");
					recv(accept_file_descriptor, buffer_2, 1024, MSG_DONTWAIT);
					value = buffer_2;
				}

				send(accept_file_descriptor, "HTTP/1.0 200 OK\r\n", strlen("HTTP/1.0 200 OK\r\n"), 0);							     		
				char *key = file_name + 4;
				FILE *fifo_file = fopen(fifo_location, "w");
				fprintf(fifo_file, "set %s %s", key, value);
				fclose(fifo_file);

			}

			close(accept_file_descriptor);

//			printf("This is the final val of the buffer: %s\n", buffer);
			exit(0);
		}
	}
}

