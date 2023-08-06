#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	FILE *file;
	char str[513];

	if (argc == 2) { // assumed that argv[0] is the program name and argv[1] is the file name, which is what we want -> valid input
		file = fopen(argv[1], "r");
		if (file == NULL) {
         	       printf("This file does not exist in this directory.");
                	exit(0);
		}
        } else if (argc > 2) 	{ // more than one command line argument entered 
		printf("Invalid input. Enter only one command line argument.");
		exit(0);
	} else { // no input file provided, read from stdin
		file = stdin;
	}


	char prev_line[513] = {0};
        char curr_line[513]; //these are buffers which are temp placeholders basically

	while (fgets(curr_line, 513, file) != NULL) {
	
		if (strcmp(prev_line, curr_line) != 0) { // if the previous line and the current line are not equal 
			printf("%s", curr_line);
			
			strcpy(prev_line, curr_line); // set prev_line to curr_line 
		}
	}	

	fclose(file);
	
	return 0;



}
