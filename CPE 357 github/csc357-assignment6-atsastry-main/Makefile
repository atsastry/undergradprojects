CC=gcc
CFLAGS= -Wall -std=c99 -pedantic -g
MAIN: httpd kvstore
OBJ = httpd.o 
KVSTOREOBJS = kvstore.o hash.o

all: $(MAIN) 

%.o: %.c 
	$(CC) -c -o $@ $< $(CFLAGS)

kvstore: $(KVSTOREOBJS)
	$(CC) $(CFLAGS) -o kvstore $(KVSTOREOBJS)

httpd: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

clean:
	rm *.o $(MAIN) core httpd db_* fifo_* kvstore
