; SPDX-License-Identifier: BSD-3-Clause

extern printf
extern get_max

section .data
    arr: dd 19, 7, 129, 87, 54, 218, 67, 12, 19, 99
    len: equ $-arr
    pos: dd 0

    print_format: db "max: %u on position: %u", 13, 10, 0

section .text

global main

main:
    push ebp
    mov ebp, esp

    ; Compute length in eax.
    ; Divide by 4 (we are using integer data type of 4 bytes) by
    ; using shr 2 (shift right with 2 bits).
    mov eax, len
    shr eax, 2

    push pos
    push eax
    push arr
    call get_max
    add esp, 12

    ; Print max.
    push dword [pos]
    push eax
    push print_format
    call printf
    add esp, 12

    leave
    ret
