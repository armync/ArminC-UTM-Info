%include "../utils/printf32.asm"

section .text
extern printf
global main
main:
    push ebp
    mov ebp, esp

    mov eax, 211    ; to be broken down into powers of 2
    mov ebx, 1      ; stores the current power

etic:
    cmp ebx, eax
    jg exit
    test ebx, eax
    jz incr
    PRINTF32 `%u\n\x0`, ebx

incr:
    shl ebx,1
    jmp etic

exit:
    leave
    ret
