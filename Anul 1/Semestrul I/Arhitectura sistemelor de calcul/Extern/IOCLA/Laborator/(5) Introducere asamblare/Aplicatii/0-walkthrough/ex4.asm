%include "printf32.asm"

section .text
    global main
    extern printf

main:
    mov eax, 1
    mov ebx, 1
    cmp eax, ebx
    add ecx, 1                  ; Comenteaza aceasta linie
    je print
    ret

print:
    PRINTF32 `%d\n\x0`, eax
    ret
