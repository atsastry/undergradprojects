#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
	//make sure input is a file name 
	//read from stdin if no file is specified 
	//check if file is null
	
	FILE *file;
	int count_newline = 0;
        int count_words = 0;
        int count_bytes = 0;
        char ch;
        int in_word = 0;

	if (argc > 2) {
		printf("Invalid input. Please only enter one command line argument.");
		return 1;
	}
	if (argc == 2) { // assumed argv[0] is the program name and argv[1] is the name of the file 
		file = fopen(argv[1], "r");
		if (file == NULL) {
			printf("This file is not in this directory.");
			return 1;
		}
	} else {
		file = stdin;
	}
	
	while (1) { 
		ch = fgetc(file);
		if (feof(file)) { //feof checks for the end of the file 
			break;
		}
			
		count_bytes++;
		if (ch == '\n') {
			count_newline++;
		}
		if (isspace(ch) == 0  && !in_word) {  
			count_words++;
			in_word = 1;
		} else if (isspace(ch) != 0) { 
			in_word = 0;
		}
		 
	}

	printf("%d %d %d\n", count_newline, count_words, count_bytes);
	fclose(file);

	return 0;	
}
