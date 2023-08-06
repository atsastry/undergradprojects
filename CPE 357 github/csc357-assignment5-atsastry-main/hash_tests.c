#include "hash.h"
#include "checkit.h"

void test1() {
	Hash* hash = makeHash();
	setHash(hash, "a", 1);
	long int val = getHash(hash, "a");
	checkit_int(val, 1);
}

int main() {
	test1();
	return 0;
}
