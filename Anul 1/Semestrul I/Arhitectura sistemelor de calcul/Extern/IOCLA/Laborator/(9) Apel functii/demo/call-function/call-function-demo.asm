;
; Author: Gabriel Mocanu <gabi.mocanu98@gmail.com>
;

section .rodata
    mystring db "This is my string", 0
    print_format db "%d + %d = %d", 10, 0

section .text

extern puts
extern printf
extern strlen

; printf("%d + %d = %d\n", 2, 5, 7);

; void sum(int a, int b, int *sum)
sum:
    push ebp
    mov ebp, esp

    mov eax, [ebp + 8]
    mov ebx, [ebp + 12]
    add eax, ebx

    mov ecx, [ebp + 16]
    mov [ecx], eax

    leave
    ret

global main
main:
    push ebp
    mov ebp, esp
    sub esp, 12

    mov dword [ebp - 4], 2
    mov dword [ebp - 8], 5

    lea ebx, [ebp - 12]
    push ebx
    push dword [ebp - 8]
    push dword [ebp - 4]
    call sum
    add esp, 12

    push dword [ebp - 12]
    push dword [ebp - 8]
    push dword [ebp - 4]
    push print_format
    call printf
    add esp, 16

    push mystring
    call puts
    add esp, 4

    leave
    ret
