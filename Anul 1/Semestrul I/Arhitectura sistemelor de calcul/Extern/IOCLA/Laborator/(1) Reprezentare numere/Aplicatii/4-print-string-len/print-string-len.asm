%include "../../utils/printf32.asm"

section .data
    mystring db "This is my string", 0
    print_format db "String length is %d", 10, 0

section .text

extern printf
global main

main:
    push ebp
    mov ebp, esp

    mov eax, mystring
    xor ecx, ecx
test_one_byte:
    mov bl, byte [eax]
    test bl, bl
    jz out
    inc eax
    inc ecx
    jmp test_one_byte

out:
    PRINTF32 `[PRINTF32]: %d\n[printf]: \x0`, ecx

    push ecx
    push print_format
    call printf
    add esp, 8

    leave
    ret
