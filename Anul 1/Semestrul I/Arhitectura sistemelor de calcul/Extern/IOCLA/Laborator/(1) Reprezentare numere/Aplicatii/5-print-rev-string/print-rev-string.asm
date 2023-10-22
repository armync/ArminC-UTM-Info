section .data
    mystring db "This is my string", 0
    print_format db "String length is %d", 10, 0
    store_string times 64 db 0

section .text

extern printf
extern puts
global main

reverse_string:
    push ebp
    mov ebp, esp

    mov eax, dword [ebp+8]
    mov ecx, dword [ebp+12]
    add eax, ecx
    dec eax
    mov edx, dword [ebp+16]

copy_one_byte:
    mov bl, byte [eax]
    mov byte [edx], bl
    dec eax
    inc edx
    loopnz copy_one_byte

    inc edx
    mov byte [edx], 0

    leave
    ret

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
    ; save ecx's value since it can be changed by printf
    push ecx

    push ecx
    push print_format
    call printf
    add esp, 8

    pop ecx

    push store_string
    push ecx
    push mystring
    call reverse_string
    add esp, 12

    push store_string
    call puts
    add esp, 4

    leave
    ret
