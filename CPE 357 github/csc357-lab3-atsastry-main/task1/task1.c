#include "task1.h"
#include <ctype.h>
#include <wctype.h>
#include <stdio.h>

	void str_lower(char *orig, char *copy) {
		// orig is the og input string and copy is the lowercase version of the string
		int i = 0;
		while (orig[i] != '\0') {
			copy[i] = tolower(orig[i]);
			printf("%c", copy[i]);
			printf("%c", orig[i]);
			i++;
		}
		copy[i] = '\0';
	}



	void str_lower_mutate(char *orig) {
		int i = 0;
		while (orig[i] != '\0') {
			orig[i] = towlower(orig[i]);
			i++;
		}
	//	orig[i] = '\0';
	}


