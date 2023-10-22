CFLAGS = -fno-PIC -m32 -g
LDFLAGS = -no-pie -m32

.DEFAULT_GOAL: all

.PHONY: all clean

all: hello

hello: hello.o
	$(CC) $(LDFLAGS) -o $@ $^

hello.o: hello.c

clean:
	-rm -f hello hello.o
	-rm -f *~
