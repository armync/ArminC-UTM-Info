CFLAGS = -fno-PIC -m32 -g
LDFLAGS = -no-pie -m32

.DEFAULT_GOAL: all

.PHONY: all clean

all: main

main: main.o hidden.o plain.o
	$(CC) $(LDFLAGS) -o $@ $^

main.o: main.c ops.h

hidden.o: hidden.c

plain.o: plain.c

clean:
	-rm -f main main.o hidden.o plain.o
	-rm -f *~
