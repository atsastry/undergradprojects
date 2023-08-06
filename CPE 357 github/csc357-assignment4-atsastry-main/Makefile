CC = gcc
CFLAGS = -Wall -std=c99 -pedantic
MAIN = a4download
OBJS = a4download_tests.o a4download.o

all : $(MAIN)

$(MAIN) : $(OBJS) a4download.h
	$(CC) $(CFLAGS) -o $(MAIN) $(OBJS)

a4download_tests.o : a4download_tests.c a4download.h
	$(CC) $(CFLAGS) -c a4download_tests.c

a4download.o : a4download.c a4download.h
	$(CC) $(CFLAGS) -c a4download.c

test: $(MAIN)
	(./a4download_tests | grep -i "failed") || echo "Tests passed"

clean :
	rm *.o $(MAIN) core file*
