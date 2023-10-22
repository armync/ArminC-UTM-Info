CFLAGS = -fno-PIC -m32 -g
LDFLAGS = -no-pie -m32

.DEFAULT_GOAL: all

.PHONY: all clean

all: main

main: main.o mul.o div.o
	$(CC) $(LDFLAGS) -o $@ $^

main.o: main.c ops.h

mul.o: mul.c

div.o: div.c

clean:
	-rm -f main main.o mul.o div.o
	-rm -f *~
