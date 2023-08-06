#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
	// requirement 1
	if (argc != 3) {
		printf("You must have 3 command line arguments.");
		return -1;
	} 
	int num_processes = atoi(argv[2]); //converting argv[2] to int
	if (num_processes <= 0) {
		printf("Invalid number of processes.");
		return -1;
	}

	// requirement 2
	FILE *file = fopen(argv[1], "r");
	if (file == NULL) {
		exit(0);
	} 
	char str[1024];
	
	int processes_counter = 0;
	int download_counter = 0;
	while (1) {
		if (fgets(str, 1024, file) == NULL) {
			break;
		}
		char file_name[1024];
		char url[1024];
		char max_download[10];
		int inputs = sscanf(str, "%s %s %s", file_name, url, max_download);
		if (inputs < 2) {
			break;
		}
		// requirement 3
		// first, fork --> duplicate process created
		download_counter++;
		pid_t process_id = fork();
		
		if (process_id == 0) { //this is the child
			int res;
			//printf("%s %s\n", file_name, url);
			if (inputs == 2) {
				res = execlp("curl", "curl", "-o", file_name, "-s", url, NULL);
			} else {
			//	printf("HELLO\n");
				res = execlp("curl","curl", "-m", max_download, "-o", file_name, "-s", url, NULL);
			}
			printf("exec failed error code%d", res);
			exit(-1);
		} else {
			printf("Process %d processing line #%d\n", process_id, download_counter); 
			processes_counter++;
				
			int wstatus;
			if (processes_counter == num_processes) {
				pid_t waiting_res = wait(&wstatus);					
				processes_counter--;
				if (waiting_res == -1) {
					printf("Process was terminated abnormally.");
				}
			}		
		}
	
	}
	int wstatus;
	while (processes_counter != 0) {
		pid_t waiting_res = wait(&wstatus);					
		processes_counter--;
		if (waiting_res == -1) {
			printf("Process was terminated abnormally.");
		}
	}
	fclose(file);
}
