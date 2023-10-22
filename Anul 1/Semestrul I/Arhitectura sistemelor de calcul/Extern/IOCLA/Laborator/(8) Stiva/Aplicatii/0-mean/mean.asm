%include "../utils/printf32.asm"

%define ARRAY_SIZE 13
%define DECIMAL_PLACES 5

section .data

    num_array dw 76, 12, 65, 19, 781, 671, 431, 761, 782, 12, 91, 25, 9

section .text

extern printf
global main
main:
    xor eax, eax
    mov ecx, ARRAY_SIZE
add_element:
    mov bx, word [num_array + (ecx - 1) * 2]
    add ax, bx
    loop add_element
    PRINTF32 `Sum of numbers: %d\n\x0`, eax
    ; Compute mean quotient.
    xor edx, edx
    mov bx, ARRAY_SIZE
    div bx
    PRINTF32 `Mean of numbers: %d\x0`, eax

    mov ecx, DECIMAL_PLACES
compute_decimal_place:
    mov ax, dx
    mov bx, 10
    mul bx
    mov bx, ARRAY_SIZE
    div bx
    PRINTF32 `%d\x0`, eax
    dec ecx
    cmp ecx, 0
    jg compute_decimal_place

    PRINTF32 `\n\x0`
    xor eax, eax
    ret
