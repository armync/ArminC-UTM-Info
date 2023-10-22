CC = gcc
CFLAGS = -Wall

TARGET_EXEC = call

MKDIR_P ?= mkdir -p

SRCS := $(shell find $(SRC_DIRS) -name "*.c")
OBJS := $(SRCS:.c=.o)

$(info OBJS is $(OBJS))
$(info SRCS is $(SRCS))

$(TARGET_EXEC): $(OBJS)
	$(CC) $(OBJS) -o $@

.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

.PHONY: clean

clean:
	$(RM) -r *.o $(TARGET_EXEC)
