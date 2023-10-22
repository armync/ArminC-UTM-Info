;
; Author: Gabriel Mocanu <gabi.mocanu98@gmail.com>
;


%include "printf32.asm"

section .text
    global main
    extern printf

main:
    push 0
    popf

    mov eax, 0
    test eax, eax

    push 0
    popf

    mov ebx, 0xffffffff
    test ebx, ebx

    push 0
    popf

    mov al, 250
    mov bl, 10
    add al, bl

    push 0
    popf

    mov al, 0
    mov bl, 1
    sub al, bl

    push 0
    popf

    mov al, 120
    mov bl, 120
    add al, bl

    push 0
    popf

    mov al, 129
    mov bl, 129
    add al, bl


    PRINTF32 `%d\n\x0`, eax
    ret
