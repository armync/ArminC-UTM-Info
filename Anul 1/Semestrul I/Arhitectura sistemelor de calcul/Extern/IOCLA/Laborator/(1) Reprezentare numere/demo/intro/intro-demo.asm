;
; Author: Gabriel Mocanu <gabi.mocanu98@gmail.com>
;

section .text

g:
    enter 0, 6

    leave
    ret
f:
    push ebp
    mov ebp, esp
    
    push 12
    call g
    add esp, 4

    leave
    ret


global main
main:
    push ebp
    mov ebp, esp

    push 10
    call f
    add esp, 4


    leave
    ret
