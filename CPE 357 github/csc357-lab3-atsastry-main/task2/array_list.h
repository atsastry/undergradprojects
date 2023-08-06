#ifndef ARRAY_LIST_H
#define ARRAY_LIST_H

#define INITIAL_CAPACITY 20

typedef struct {
        char **data; // pointer to a char pointer, we use this because we want arrays of strings aka arrays of char pointers and arrays are pointers so therefore, u need a pointer to a pointer
        int length;
        int capacity;
} ArrayList;

ArrayList *array_list_new();

void array_list_add_to_end(ArrayList *list, char *str);

#endif
