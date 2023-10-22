%include "../utils/printf32.asm"

%define NUM_FIBO 10

section .text

extern printf
global main
main:
    mov ebp, esp

    push 0
    push 1

    mov ecx, NUM_FIBO - 2

calc_fibo:
    mov eax, [esp]
    add eax, [esp + 4]
    push eax
    loop calc_fibo

    mov ecx, NUM_FIBO
print:
    mov eax, dword [esp + (ecx - 1) * 4]
    PRINTF32 `%d \x0`, eax
    dec ecx
    cmp ecx, 0
    ja print

    PRINTF32 `\n\x0`
    mov esp, ebp
    xor eax, eax
    ret
