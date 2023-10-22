%include "printf32.asm"

section .data
source_text: db "ABCABCBABCBABCBBBABABBCBABCBAAACCCB", 0
substring: db "BABC", 0

print_format: db "Substring found at index: %d", 10, 0

section .text
extern printf
global main
main:
    push ebp
    mov ebp, esp

    mov esi, source_text
    mov edi, substring

source_loop:
    mov eax, esi
    mov edx, edi

substr_loop:
    cmp byte [edx], 0
    je found_substr
    mov bl, byte [eax]
    cmp byte [edx], bl
    jne exit_substr_loop
    inc eax
    inc edx
    jmp substr_loop

found_substr:
    pusha
    mov ecx, esi
    sub ecx, source_text
    push ecx
    push print_format
    call printf
    add esp, 8
    popa

exit_substr_loop:
    inc esi
    cmp byte [esi], 0
    je exit
    jmp source_loop

exit:
    leave
    ret
