%include "printf32.asm"

section .text
    global main
    extern printf

main:
    mov eax, 4
    PRINTF32 `%d\n\x0`, eax

jump_incoming:
    jmp exit                    ; salt neconditionat catre label-ul exit

    mov eax, 7                  ; codul acesta nu se executa
    mov ebx, 8
    add eax, ebx
    PRINTF32 `%d\n\x0`, eax

exit:
    ret
