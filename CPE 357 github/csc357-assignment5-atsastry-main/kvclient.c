#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

void usage() {
	printf("./kvclient <named pipe> <get or set> <key> [<value>]");
	exit(-1);
}


int main(int argc, char *argv[]) {
	if (argc < 4) {
		usage();
	} else if ((argc == 4) && strcmp(argv[2], "get") == 0) {
		// return value
		// open the pipe for writing
		pid_t process_id = getpid();
		FILE *pipe = fopen(argv[1], "w");
		fprintf(pipe, "get %d %s", process_id, argv[3]);	
		fclose(pipe);
		// wait for the other pipe to open and read from it and print the ouput
		
		char fifo_name[1024];
		sprintf(fifo_name, "fifo_%d", process_id);
		FILE *pipe_reading = fopen(fifo_name, "r");
		while (pipe_reading == NULL) {
			pipe_reading = fopen(fifo_name, "r");
		}
		char str[1024];
		fgets(str, 1024, pipe_reading);
		fclose(pipe_reading);
		remove(fifo_name);
		printf("%s", str);

	} else if ((argc == 5) && strcmp(argv[2], "set") == 0) {
		// set the value to 4th command line arg
		FILE *pipe = fopen(argv[1], "w");
		fprintf(pipe, "set %s %s", argv[3], argv[4]);
		fclose(pipe);
	} else {
		usage();
	}
}

	
