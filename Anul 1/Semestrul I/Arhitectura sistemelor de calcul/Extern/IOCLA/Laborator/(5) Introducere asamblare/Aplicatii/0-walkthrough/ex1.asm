%include "printf32.asm"

section .text
    global main
    extern printf

main:
    mov eax, 7                  ; incarca in registrul eax valoarea 7
    mov ebx, 8                  ; incarca in registrul ebx valoarea 8
    add eax, ebx                ; aduna valoarea ce se afla in registrul eax
                                ; cu valoarea ce se afla in registrul ebx si
                                ; stocheaza rezultatul in eax
    PRINTF32 `%d\n\x0`, eax     ; printeaza valoarea din registrul eax
