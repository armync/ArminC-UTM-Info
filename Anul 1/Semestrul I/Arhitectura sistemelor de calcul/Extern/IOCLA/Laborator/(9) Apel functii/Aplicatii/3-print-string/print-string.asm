%include "../utils/printf32.asm"

section .data
    mystring db "This is my string", 0

section .text

extern puts
extern printf
global main
main:
    push ebp
    mov ebp, esp

    PRINTF32 `[PRINTF32]: %s\n[PUTS]: \x0`, mystring


    push mystring
    call puts
    add esp, 4

    leave
    ret
