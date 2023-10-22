CFLAGS = -fno-PIC -m32 -g
LDFLAGS = -static -no-pie -m32

.DEFAULT_GOAL: all

.PHONY: all clean

all: name

name: name.o
	$(CC) $(LDFLAGS) -o $@ $^
	#ld -static -m elf_i386 -L/usr/lib/gcc/x86_64-linux-gnu/7/32/ -o $@ /usr/lib32/crt1.o /usr/lib32/crti.o $^ --start-group -lc -lgcc -lgcc_eh --end-group /usr/lib32/crtn.o

name.o: name.c

clean:
	-rm -f name name.o
	-rm -f *~
