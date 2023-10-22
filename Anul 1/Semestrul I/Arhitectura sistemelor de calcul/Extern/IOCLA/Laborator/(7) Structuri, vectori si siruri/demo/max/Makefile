NASM = nasm
AFILES = max.asm
OBJS = $(AFILES:.asm=.o)
ASM_FLAGS = -f elf32 -g
LD=gcc
LDFLAGS = -m32 -g
BINARIES = max

all : $(BINARIES)

%.o : %.asm
	$(NASM) $(ASM_FLAGS) -o $@ $<

clean:
	rm -f *.o $(BINARIES) *.s
	rm -f *~
