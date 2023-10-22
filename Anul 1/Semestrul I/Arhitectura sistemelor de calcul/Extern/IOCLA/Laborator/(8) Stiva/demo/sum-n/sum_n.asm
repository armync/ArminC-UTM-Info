%include "../utils/printf32.asm"

section .text
extern printf
global main

main:
        push    ebp
        mov     ebp, esp

        ; ecx <- i (number / increment)
        ; eax <- sum
        ; init i (i <- 100)
        mov ecx, 100
        ; init sum (sum <- 0)
        xor eax, eax   ; mov eax, 0

.L3:
        add eax, ecx
        loop .L3    ; dec ecx; cmp ecx, 0; jne .L3

        PRINTF32 `%u\n\x0`, eax
        mov     eax, 0
        pop     ebp
        ret
