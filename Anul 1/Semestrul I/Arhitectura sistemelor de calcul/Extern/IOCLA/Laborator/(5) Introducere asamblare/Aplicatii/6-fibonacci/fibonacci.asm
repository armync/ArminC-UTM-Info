%include "printf32.asm"

section .text
    global main
    extern printf

main:
    mov ecx, 7       ; vrem sa aflam al N-lea numar; N = 7
    ; TODO: calculati al N-lea numar fibonacci (f(0) = 0, f(1) = 1)
    mov eax, 0
    mov ebx, 1

fibonacci:
    dec ecx
    test ecx, ecx
    je print
    add eax, ebx
    xchg eax, ebx
    jmp fibonacci

print:
    PRINTF32 `%d\n\x0`, ebx
    xor eax, eax
    ret
