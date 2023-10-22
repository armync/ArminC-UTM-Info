%include "../../utils/printf32.asm"

section .data
    array dw 10, 20, 30, 17, 277, 127, 17792, 1781, 2891, 2129
    len equ 10

section .text
extern printf
global main

main:
    push ebp
    mov ebp, esp

    ; ecx -> iterator through vector (ecx -> 0..9)
    xor ecx, ecx

    ; edx -> store max
    xor edx, edx

again:
    cmp dx, [array + 2*ecx]
    ja noaction

    ; Load new value in edx (max).
    mov dx, [array + 2*ecx]

noaction:
    inc ecx
    cmp ecx, len
    jb again

    PRINTF32 `%u\x0`, edx

    xor eax, eax
    leave
    ret
