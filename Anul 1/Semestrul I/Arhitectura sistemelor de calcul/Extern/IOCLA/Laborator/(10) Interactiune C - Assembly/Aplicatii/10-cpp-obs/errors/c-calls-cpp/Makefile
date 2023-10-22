CFLAGS = -Wall -g
CXXFLAGS = -Wall -g
LDFLAGS = -lstdc++

.DEFAULT_GOAL: all

.PHONY: all clean

all: main

main: main.o add.o sub.o
	$(CC) $(LDFLAGS) -o $@ $^

main.o: main.c ops.h

add.o: add.cpp

sub.o: sub.cpp

clean:
	-rm -f main main.o add.o sub.o
	-rm -f *~
