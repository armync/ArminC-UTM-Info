CFLAGS = -fno-PIC -m32 -g
LDFLAGS = -no-pie -m32

.DEFAULT_GOAL: all

.PHONY: all clean

all: hello

hello: hello.o
	$(CC) $(LDFLAGS) -o $@ $^
	#ld -dynamic-linker /lib/ld-linux.so.2 -m elf_i386 -o $@ /usr/lib32/crt1.o /usr/lib32/crti.o $^ -lc /usr/lib32/crtn.o

hello.o: hello.c

clean:
	-rm -f hello hello.o
	-rm -f *~
