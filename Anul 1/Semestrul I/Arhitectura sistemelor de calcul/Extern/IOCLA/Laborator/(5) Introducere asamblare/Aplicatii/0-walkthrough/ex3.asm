%include "printf32.asm"

section .text
    global main
    extern printf

main:
    mov eax, zone2
    jmp eax                     ; salt neconditionat catre adresa
                                ; ce se afla in registrul eax
zone1:
    mov eax, 1
    mov ebx, 2
    add eax, ebx
    PRINTF32 `%d\n\x0`, eax
jump1:
    jmp exit

zone2:
    mov eax, 7
    mov ebx, 8
    add eax, ebx
    PRINTF32 `%d\n\x0`, eax
jump2:
    jmp $-0x4A                 ; salt relativ cu deplasamanent

exit:
    ret
