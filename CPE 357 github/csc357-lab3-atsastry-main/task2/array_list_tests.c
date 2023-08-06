#include "checkit.h"
#include "array_list.h"
#include <stdio.h>
#include <stdlib.h>

void test1() { // test for array_list_new
	ArrayList *array_list = array_list_new();
	checkit_int(array_list->capacity, INITIAL_CAPACITY);
	checkit_int(array_list->length, 0);
	free(array_list);
}

void test2() { // test for array_list_add_to_end
	ArrayList *array_list = array_list_new();
	char *str = "a";
	array_list_add_to_end(array_list, str);
	checkit_int(array_list->length, 1);
	checkit_string(array_list->data[0], "a");
	free(array_list);
}

void test3() {
	ArrayList *array_list = array_list_new();
	char str[21];
	for (int i = 0; i < INITIAL_CAPACITY + 1; i++) {
		sprintf(str, "%d\n", i);
		char *copy = malloc(strlen(str+1));		
		strcpy(copy, str);
		array_list_add_to_end(array_list, copy);
	}

	checkit_int(array_list->capacity, 2 * INITIAL_CAPACITY);
	checkit_int(array_list->length, 1 + INITIAL_CAPACITY);
	checkit_string(array_list->data[0], "0\n");
}



int main() {
	test1();	
	test2();
	test3();
	return 0;
}
