extern printf

section .rodata

    array: dd 181, 288, 2743, 327, 27, 2773, 283, 228
    fmt_str: db "min is: %u", 10, 0
    len equ 8

section .text

global main

; equivalent to unsigned int min_fn(unsigned int *array, unsigned int len);
min_fn:
    push ebp
    mov ebp, esp

    ; ebx <- array
    ; ecx <- len
    mov ebx, [ebp+8]
    mov ecx, [ebp+12]

    ; eax stores the maximum unsigned int value.
    ; equivalent to mov eax, 0xffffffff
    xor eax, eax
    dec eax

again:
    ; compare current minimum with array[ecx-1]
    cmp eax, [ebx + 4*ecx - 4]
    jb noaction
    mov eax, [ebx + 4*ecx - 4]
noaction:
    loop again

    leave
    ret


main:
    push ebp
    mov ebp, esp


    ; min = min_fn(array, len)
    ; eax <- min (return value)
    push len
    push array
    call min_fn
    add esp, 8


    ; printf(fmt_str, min)
    ; min is in eax
    push eax
    push fmt_str
    call printf
    add esp, 8


    leave
    ret
