;
; IOCLA, Buffer management
;
; Fill buffer with data and print it.
; Buffer is stored in .data section (initialized data).
;

extern printf
extern puts

section .data
    buffer: times 64 db 5
    len: equ $-buffer

    buffer_intro_message: db "buffer is:", 0
    byte_format: db " %02X", 0
    null_string: db 0

section .text

global main

main:
    push ebp
    mov ebp, esp

    ; Fill data in buffer: buffer[i] = i+1
    ; ecx is buffer index (i), dl is buffer value (i+1). dl needs to be ecx+1.
    ; Buffer length is 64 bytes.
    xor ecx, ecx
fill_byte:
    mov dl, cl
    inc dl
    mov byte [buffer+ecx], dl
    inc ecx
    cmp ecx, len
    jl fill_byte

    ; Print data in buffer.
    push buffer_intro_message
    call printf
    add esp, 4

    xor ecx, ecx
print_byte:
    xor eax, eax
    mov al, byte[buffer+ecx]
    push ecx	; save ecx

    ; Print current byte.
    push eax
    push byte_format
    call printf
    add esp, 8

    pop ecx	; restore ecx
    inc ecx
    cmp ecx, len
    jl print_byte

    ; Print new line. C equivalent instruction is puts("").
    push null_string
    call puts
    add esp, 4

    leave
    ret
