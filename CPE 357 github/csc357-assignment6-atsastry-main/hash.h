#ifndef HASH_H  // if its not defined
#define HASH_H 
#define NODES_SIZE 10169
typedef struct Node {
	long int value; // originally char value[1025]
	struct Node *next;
	char key[33];
} Node;


typedef struct Hash {
	Node *nodes[NODES_SIZE];
	
} Hash;

Hash* makeHash(); // implementations in .c
void setHash(Hash* hash, char *key, long int value);
long int  getHash(Hash* hash, char *key);
Node* getAllKeys(Hash *hash);
void destroyHash(Hash* hash);






#endif


