CC = gcc
CFLAGS = -Wall -std=c99 -pedantic
MAIN = kvstore 
OBJS = kvstore.o hash.o

all : $(MAIN) kvclient

$(MAIN) : $(OBJS) 
	$(CC) $(CFLAGS) -o $(MAIN) $(OBJS)
kvclient: kvclient.o
	$(CC) $(CFLAGS) -o kvclient kvclient.o

hash_tests.o : hash_tests.c hash.h
	$(CC) $(CFLAGS) -c hash_tests.c

kvstore.o: kvstore.c 
	$(CC) $(CFLAGS) -c kvstore.c

kvclient.o: kvclient.c
	$(CC) $(CFLAGS) -c kvclient.c
hash.o: hash.c hash.h
	$(CC) $(CFLAGS) -c hash.c 

#hash_tests: hash_tests.o
#	$(CC) $(CLFAGS) -o hash_tests hash_tests.o hash.o

test: $(MAIN)
	(./hash_tests | grep -i "failed") || echo "Tests passed"

clean :
	rm *.o $(MAIN) core db_* fifo_* kvclient hash_tests
