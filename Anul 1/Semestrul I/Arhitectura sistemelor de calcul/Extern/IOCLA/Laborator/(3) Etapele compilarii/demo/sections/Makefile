CFLAGS = -Wall -fno-stack-protector -fno-PIC
LDFLAGS_STATIC = -static -no-pie
LDFLAGS = -no-pie


.PHONY: all clean

all: sections-dynamic sections-static

sections-dynamic: sections.o
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS)

sections-static: sections.o
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS_STATIC)

sections.o: sections.c

clean:
	-rm -f *.o sections-dynamic sections-static
	-rm -f *~
