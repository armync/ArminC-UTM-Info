;
; IOCLA, Buffer management
;
; Fill buffer with data and print it. Buffer is 64 bytes long and
; is stored on the stack.
;

extern printf
extern puts

section .data
    buffer_intro_message: db "buffer is:", 0
    byte_format: db " %02X", 0
    null_string: db 0
    var_message_and_format: db "var is 0x%08X", 13, 10, 0

section .text

global main

main:
    push ebp
    mov ebp, esp

    ; Make room for local variabile (32 bit, 4 bytes).
    ; Variable address is at ebp-4.
    sub esp, 4

    ; Make room for buffer (64 bytes).
    ; Buffer address is at ebp-68.
    sub esp, 64

    ; Initialize local variable.
    mov dword [ebp-4], 0xCAFEBABE

    ; Fill data in buffer: buffer[i] = i+1
    ; Use ebx as buffer base address, ecx as index and dl as value.
    ; dl needs to be ecx+1.
    ; Buffer length is 64 bytes.
    lea ebx, [ebp-68]
    xor ecx, ecx
fill_byte:
    mov dl, cl
    inc dl
    mov byte [ebx+ecx], dl
    inc ecx
    cmp ecx, 64
    jl fill_byte

    ; solution 4
    mov dword [ebx+ecx], 0xDEADBEEF

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
    push byte_format
    call printf
    add esp, 8

    pop ecx	; restore ecx
    inc ecx
    cmp ecx, 76 ; solution 3
    jl print_byte

    ; Print new line. C equivalent instruction is puts("").
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
