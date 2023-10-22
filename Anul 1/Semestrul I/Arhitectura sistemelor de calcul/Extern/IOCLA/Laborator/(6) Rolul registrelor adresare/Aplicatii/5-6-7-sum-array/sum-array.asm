%include "../utils/printf32.asm"

%define ARRAY_SIZE    10

section .data
    byte_array db 8, 19, 12, 3, 6, 200, 128, 19, 78, 102
    word_array dw 1893, 9773, 892, 891, 3921, 8929, 7299, 720, 2590, 28891
    dword_array dd 1392849, 12544, 879923, 8799279, 7202277, 971872, 28789292, 17897892, 12988, 8799201

section .text
extern printf
global main
main:
    push ebp
    mov ebp, esp

    mov ecx, ARRAY_SIZE     ; Use ecx as loop counter.
    xor eax, eax            ; Use eax to store the sum.
    xor edx, edx            ; Store current value in dl; zero entire edx.

add_byte_array_element:
    mov dl, byte [byte_array + ecx - 1]
    add eax, edx
    loop add_byte_array_element ; Decrement ecx, if not zero, add another element.

    PRINTF32 `Array sum is %u\n\x0`, eax

    mov ecx, ARRAY_SIZE
    xor eax, eax
    xor edx, edx
add_word_array_element:
    mov dx, word [word_array + 2 * ecx - 2]
    add eax, edx
    loop add_word_array_element ; Decrement ecx, if not zero, add another element.

    PRINTF32 `Array sum is %u\n\x0`, eax

    mov ecx, ARRAY_SIZE
    xor eax, eax
    xor edx, edx

add_dword_array_element:
    mov edx, dword [dword_array + 4 * ecx - 4]
    add eax, edx
    loop add_dword_array_element ; Decrement ecx, if not zero, add another element.

    PRINTF32 `Array sum is %u\n\x0`, eax

    leave
    ret
