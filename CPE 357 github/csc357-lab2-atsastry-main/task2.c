#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	
	FILE *file;
        if (argc == 2) { // assumed that argv[0] is the program name and argv[1] is the file name, which is what we want -> valid input
                file = fopen(argv[1], "r");
                if (file == NULL) {
                       printf("This file does not exist in this directory.");
                        exit(0);
                }
        } else { // no input file provided, read from stdin 
                printf("Invalid input. Enter exactly one command line argument.");
                exit(0);

	}

	// count the number of spaces and tabs
	int space_counter = 0;
	int tab_counter = 0;
	int ch;
	while ((ch = fgetc(file)) != EOF) { //fgetc reads character at a time
		if (ch == ' ') {
			space_counter++;
		}
		if (ch == '\t') {
			tab_counter++;
		}
	}

	fclose(file); //close the file
	printf("Number of spaces in this file: %d\n",space_counter);
	printf("Number of tabs in this file: %d\n", tab_counter);
	return 0; 

}
