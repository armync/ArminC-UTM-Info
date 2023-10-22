%include "../utils/printf32.asm"

section .data
    i: dd 0
    sum: dd 0

section .text
extern printf
global main

main:
        push    ebp
        mov     ebp, esp
        mov     dword [i], 1
.L3:
        mov     eax, [i]
        cmp     eax, 100
        ja      .L2
        mov     edx, [sum]
        mov     eax, [i]
        add     eax, edx
        mov     [sum], eax
;        mov     eax, [i]
;        add     eax, 1
;        mov     [i], eax
        inc dword [i]
        jmp     .L3
.L2:
        PRINTF32 `%u\n\x0`, dword [sum]
        mov     eax, 0
        pop     ebp
        ret
