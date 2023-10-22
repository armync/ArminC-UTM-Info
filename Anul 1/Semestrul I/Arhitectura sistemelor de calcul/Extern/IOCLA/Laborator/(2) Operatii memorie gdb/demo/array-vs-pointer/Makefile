CFLAGS = -m32 -fno-PIC -Wall
LDFLAGS = -m32 -no-pie

.PHONY: all clean

all: array_vs_pointer

array_vs_pointer: array_vs_pointer.o

array_vs_pointer.o: array_vs_pointer.c

clean:
	-rm -f *~
	-rm -f array_vs_pointer.o array_vs_pointer
