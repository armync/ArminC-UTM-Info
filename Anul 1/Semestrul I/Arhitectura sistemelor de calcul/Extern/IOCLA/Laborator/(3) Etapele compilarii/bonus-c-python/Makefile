CFLAGS = -Wall -g
PYTHON = python3.9

.DEFAULT_GOAL: all

.PHONY: all clean

all: main

main: main.o
	gcc main.o -o main -l$(PYTHON)

main.o: main.c
	gcc -I/usr/include/$(PYTHON)/ -c main.c -o main.o

run:
	./main

clean:
	-rm -f main main.o
	-rm -f *~
