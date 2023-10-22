%include "printf32.asm"

section .data
    N dd 9 ; compute the sum of the first N fibonacci numbers
    sum_print_format db "Sum first %d fibonacci numbers is %d", 10, 0

section .text
extern printf
global main
main:
    push ebp
    mov ebp, esp

    ; The calling convention requires saving and restoring `ebx` if modified
    push ebx

    xor eax, eax     ;store the sum in eax
    mov ecx, [N]
    mov ebx, 0
    mov edx, 1

calc_fibo:
    add eax, ebx
    add ebx, edx
    xchg ebx, edx
    ; The `xhcg` above is equivalent to the following:
    ; push eax
    ; mov eax, ebx
    ; mov ebx, edx
    ; mov edx, eax
    ; pop eax
    loop calc_fibo

    push eax
    push dword [N]
    push sum_print_format
    call printf
    add esp, 12

    ; Restore the `ebx` that was previously saved
    pop ebx

    xor eax, eax
    leave
    ret
