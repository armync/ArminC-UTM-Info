CFLAGS = -fno-PIC -m32 -g
LDFLAGS = -no-pie -m32

.DEFAULT_GOAL: all

.PHONY: all clean

all: main

main: main.o libops.a
	$(CC) $(LDFLAGS) -o $@ $< -L. -lops

main.o: main.c ops.h

libops.a: add.o sub.o
	ar rc $@ $^

add.o: add.c

sub.o: sub.c

clean:
	-rm -f main main.o libops.a add.o sub.o
	-rm -f *~
