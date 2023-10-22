CFLAGS = -Wall -fno-stack-protector -fno-PIC

.PHONY: all clean

all: hello-world

hello-world: hello-world.o
	ld -dynamic-linker /lib64/ld-linux-x86-64.so.2 \
		/usr/lib/x86_64-linux-gnu/crt1.o \
		/usr/lib/x86_64-linux-gnu/crti.o \
		-lc hello-world.o \
		/usr/lib/x86_64-linux-gnu/crtn.o \
		-o hello-world

hello-world.o: hello-world.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	-rm -f hello-world *.o
	-rm -f *~
