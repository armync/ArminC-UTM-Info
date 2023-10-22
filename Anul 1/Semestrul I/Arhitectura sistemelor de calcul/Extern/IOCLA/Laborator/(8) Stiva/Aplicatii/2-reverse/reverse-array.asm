%include "../utils/printf32.asm"

%define ARRAY_LEN 7

section .data

input dd 122, 184, 199, 242, 263, 845, 911
output times ARRAY_LEN dd 0

section .text

extern printf
global main
main:

    push ARRAY_LEN
    pop ecx
push_elem:
    push dword [input + 4 * (ecx - 1)]
    loop push_elem

    push ARRAY_LEN
    pop ecx
pop_elem:
    pop dword [output + 4 * (ecx - 1)]
    loop pop_elem

    PRINTF32 `Reversed array: \n\x0`
    xor ecx, ecx
print_array:
    mov edx, [output + 4 * ecx]
    PRINTF32 `%d\n\x0`, edx
    inc ecx
    cmp ecx, ARRAY_LEN
    jb print_array

    xor eax, eax
    ret
