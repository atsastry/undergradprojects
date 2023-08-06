#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "checkit.h"
#include "array_list.h"

ArrayList *array_list_new() { // returns a point to an ArrayList
        ArrayList *list = malloc(sizeof(ArrayList));
        list->data = malloc(INITIAL_CAPACITY * sizeof(char *));
        list->length = 0;
        list->capacity = INITIAL_CAPACITY;
        return list;
}

void array_list_add_to_end(ArrayList *list, char *str) {
        //add str to the end of list
        if (list->length == list->capacity) {
                int new_capacity = list->capacity * 2;
                char **new_data = realloc(list->data, new_capacity * sizeof(char *));
                list->data = new_data;
                list->capacity = new_capacity;
        }
	list->data[list->length] = str; // do i need to use strdup here
        list->length++;
}

