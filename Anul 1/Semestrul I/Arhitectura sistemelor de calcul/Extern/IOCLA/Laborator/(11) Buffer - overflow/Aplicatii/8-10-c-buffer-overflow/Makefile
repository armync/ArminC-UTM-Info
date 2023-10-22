# IOCLA 2016
# USO remembers

CC=gcc
CFLAGS=-m32 -masm=intel -fno-stack-protector

all: do_overflow do_overflow.asm

do_overflow: do_overflow.o
	$(CC) $(CFLAGS) -o $@ $<

do_overflow.o: do_overflow.c

do_overflow.asm: do_overflow.c
	$(CC) $(CFLAGS) -S -o $@ $^

clean:
	rm -f *.o *.asm do_overflow
