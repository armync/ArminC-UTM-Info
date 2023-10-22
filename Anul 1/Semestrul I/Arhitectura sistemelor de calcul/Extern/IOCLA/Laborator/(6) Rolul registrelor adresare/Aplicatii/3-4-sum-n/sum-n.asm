%include "../utils/printf32.asm"

section .data
    num dd 100

section .text
extern printf
global main
main:
    push ebp
    mov ebp, esp

    mov ecx, [num]     ; Use ecx as counter for computing the sum.
    xor eax, eax       ; Use eax to store the sum. Start from 0.

add_to_sum:
    add eax, ecx
    loop add_to_sum    ; Decrement ecx. If not zero, add it to sum.

    mov ecx, [num]
    PRINTF32 `Sum(%u): %u\n\x0`, ecx, eax

    leave
    ret
