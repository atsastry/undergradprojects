CC = gcc
CFLAGS = -Wall -std=c99 -pedantic
MAIN = task1_tests
OBJS = task1_tests.o task1.o

all : $(MAIN)

$(MAIN) : $(OBJS) task1.h
	$(CC) $(CFLAGS) -g  -o $(MAIN) $(OBJS)

array_list_tests.o : task1_tests.c task1.h
	$(CC) $(CFLAGS) -c task1_tests.c

array_list.o : task1.c task1.h
	$(CC) $(CFLAGS) -c task1.c

test: $(MAIN)
	(./task1_tests | grep -i "failed") || echo "Tests passed"

clean :
	rm *.o $(MAIN) core
