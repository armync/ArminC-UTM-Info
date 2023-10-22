CFLAGS = -fno-PIC -m32 -g
LDFLAGS = -no-pie -m32

.DEFAULT_GOAL: all

.PHONY: all clean

all: main

main: main.o add.o sub.o
	$(CC) $(LDFLAGS) -o $@ $^

main.o: main.c ops.h

add.o: add.c

sub.o: sub.c

clean:
	-rm -f main main.o add.o sub.o
	-rm -f *~
