CFLAGS = -Wall

.PHONY: all clean

all: static-1 static-2 static-3 static-4

static-1: static-1.o

static-1.o: static-1.c

static-2: static-2.o

static-2.o: static-2.c

static-3: static-3.o

static-3.o: static-3.c

static-4: static-41.o static-42.o
	$(CC) $(CFLAGS) -o $@ $^ 

static-41.o: static-41.c

static-42.o: static-42.c

clean:
	-rm -f static-1 static-2 static-3 static-4 *.o
	-rm -f *~
