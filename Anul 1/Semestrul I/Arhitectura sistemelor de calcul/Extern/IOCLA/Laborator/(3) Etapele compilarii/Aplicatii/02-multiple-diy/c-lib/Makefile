CFLAGS = -fno-PIC -m32 -g
LDFLAGS = -no-pie -m32

.DEFAULT_GOAL: all

.PHONY: all clean

all: main

main: main.o libops.a
	$(CC) $(LDFLAGS) -o $@ $< -L. -lops

main.o: main.c ops.h

libops.a: mul.o div.o
	ar rc $@ $^

mul.o: mul.c

div.o: div.c

clean:
	-rm -f main main.o libops.a mul.o div.o
	-rm -f *~
