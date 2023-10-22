CC=gcc

.PHONY: clean all

all: preprocess compile asamble linking

preprocess: hello-world.c
	$(CC) -E -o hello-world.i $< 

compile: hello-world.i
	$(CC) -Wall -S -masm=intel -o hello-world.s $<

asamble: hello-world.s
	$(CC) -c -o hello-world.o $<

linking: hello-world.o
	$(CC) -o hello-world $<

clean:
	rm hello-world hello-world.o hello-world.s hello-world.i
