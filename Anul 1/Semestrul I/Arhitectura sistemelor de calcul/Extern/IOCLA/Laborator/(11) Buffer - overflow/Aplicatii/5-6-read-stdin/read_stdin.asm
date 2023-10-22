;
; IOCLA, Buffer management
;
; Fill buffer with data from standard input.
; Buffer is stored on the stack.
;

extern printf
extern puts
extern strlen
extern gets

section .data
    read_message: db "insert buffer string: ", 0
    buffer_intro_message: db "buffer is:", 0
    byte_format: db " %02X(%c)", 0
    null_string: db 0
    var_message_and_format: db "var is 0x%08X", 13, 10, 0

section .text

global main

main:
    push ebp
    mov ebp, esp

    ; Make room for local variable (32 bit, 4 bytes).
    ; Variable address is at ebp-4.
    sub esp, 4

    ; Make room for buffer (64 bytes).
    ; Buffer address is at ebp-68.
    sub esp, 64

    ; Initialize local variable.
    mov dword [ebp-4], 0xCAFEBABE

    ; Read buffer from standard input.
    push read_message
    call printf
    add esp, 4

    lea ebx, [ebp-68]
    push ebx
    call gets
    add esp, 4

    ; Push string length on the stack.
    ; String length is stored at ebp-72.
    push ebx
    call strlen
    add esp, 4
    push eax

    ; Print data in buffer.
    push buffer_intro_message
    call printf
    add esp, 4

    xor ecx, ecx
print_byte:
    xor eax, eax
    lea ebx, [ebp-68]
    mov al, byte[ebx+ecx]
    push ecx	; save ecx

    ; Print current byte.
    push eax
    push eax
    push byte_format
    call printf
    add esp, 12

    pop ecx	; restore ecx
    inc ecx
    cmp ecx, [ebp-72]
    jl print_byte

    push null_string
    call puts
    add esp, 4

    ; Print local variable.
    mov eax, [ebp-4]
    push eax
    push var_message_and_format
    call printf
    add esp, 8

    leave
    ret
