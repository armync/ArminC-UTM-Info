CFLAGS = -Wall -g
CXXFLAGS = -Wall -g

.DEFAULT_GOAL: all

.PHONY: all clean

all: main

main: main.o add.o sub.o
	$(CXX) $(LDFLAGS) -o $@ $^

main.o: main.cpp ops.h

add.o: add.c

sub.o: sub.c

clean:
	-rm -f main main.o add.o sub.o
	-rm -f *~
