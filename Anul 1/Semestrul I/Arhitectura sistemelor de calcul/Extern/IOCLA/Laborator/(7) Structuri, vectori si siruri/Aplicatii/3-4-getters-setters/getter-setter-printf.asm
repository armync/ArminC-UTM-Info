%include "printf32.asm"

struc my_struct
    int_x: resb 4
    char_y: resb 1
    string_s: resb 32
endstruc

section .data
    sample_obj:
        istruc my_struct
            at int_x, dd 1000
            at char_y, db 'a'
            at string_s, db 'My string is better than yours', 0
        iend

    new_int dd 2000
    new_char db 'b'
    new_string db 'Are you sure?', 0

section .text
extern printf
global main

main:
    push ebp
    mov ebp, esp

    PRINTF32 `int_x: %d\n\x0`, [sample_obj + int_x]
    PRINTF32 `char_y: %c\n\x0`, [sample_obj + char_y]
    lea eax, [sample_obj + string_s]
    PRINTF32 `string_s: %s\n\x0`, eax

    mov eax, [new_int]
    mov [sample_obj + int_x], eax

    mov al, [new_char]
    mov [sample_obj + char_y], al

    mov ecx, 0
copy:
    mov bl, [new_string + ecx]
    mov [sample_obj + string_s + ecx], bl
    inc ecx
    cmp bl, 0
    jnz copy

    PRINTF32 `int_x: %d\n\x0`, [sample_obj + int_x]
    PRINTF32 `char_y: %c\n\x0`, [sample_obj + char_y]
    lea eax, [sample_obj + string_s]
    PRINTF32 `string_s: %s\n\x0`, eax

    xor eax, eax
    leave
    ret
