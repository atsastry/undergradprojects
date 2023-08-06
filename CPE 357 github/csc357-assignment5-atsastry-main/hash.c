#include "hash.h"
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

Hash* makeHash() {
	Hash* hash = calloc(1, sizeof(Hash));
	return hash;
}

uint32_t hashFunction(char *key) {
	uint32_t accumulator = 0;
	int i = 0;
	while (key[i] !=  '\0') {
		accumulator = ((accumulator * 31) + key[i] + accumulator) % NODES_SIZE;
		i++;
	}
	return accumulator;
}


void setHash(Hash* hash, char *key, long int value) {
	uint32_t index = hashFunction(key);
//	fprintf(stderr, "%d\n", index);
	if (hash->nodes[index] == NULL) {
		hash->nodes[index] = malloc(sizeof(Node));
		hash->nodes[index]->value = value;
		strcpy(hash->nodes[index]->key, key);
		hash->nodes[index]->next = NULL;
	} else {
		Node *new_node = malloc(sizeof(Node));
		new_node->value = value;
                strcpy(new_node->key, key);
		
                new_node->next = hash->nodes[index];
		hash->nodes[index] = new_node;
	}
}


long int getHash(Hash* hash, char *key) {
	uint32_t index = hashFunction(key);
//	fprintf(stderr, "%d\n", index);
	for (Node *node = hash->nodes[index]; node != NULL; node = node->next) {
		if (strcmp(key, node->key) == 0) {
			return node->value;
		}
	}	
	return -1;
}



Node* getAllKeys(Hash *hash) {
	Node *linked_list = NULL;
	for (int i = 0; i < NODES_SIZE; i++) {
		if(hash->nodes[i] != NULL) {
			for (Node *node = hash->nodes[i]; node != NULL; node = node->next) {
				Node *new_node = malloc(sizeof(Node));	
				new_node->value = node-> value;
				strcpy(new_node->key, node->key);
				new_node->next = linked_list;
				linked_list = new_node;
			}
		}
	}
	return linked_list;
}


void destroyHash(Hash* hash) {
	for (int i = 0; i < NODES_SIZE; i++) {
		if (hash->nodes[i] != NULL) {
			Node *node = hash->nodes[i]; 
			while (node != NULL) {
				Node *temp_node = node;
				node = node->next;
				free(temp_node);
			}
		}
	}
	free(hash);
}



