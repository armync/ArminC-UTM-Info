%include "../utils/printf32.asm"

%define ARRAY_SIZE    10

section .data
    dword_array dd 1392, 12544, 7991, 6992, 7202, 27187, 28789, 17897, 12988, 17992

section .text
extern printf
global main
main:
    mov ecx, ARRAY_SIZE     ; Use ecx as loop counter.
    xor esi, esi            ; Store even number in esi.
    xor edi, edi            ; Store odd number in edi.
next_element:

    ; We need to initialize the dividend (EDX:EAX) to 0:array_element
    xor edx, edx
    mov eax, dword [dword_array + ecx*4 - 4]
    ; Store the divisor (2) in EBX.
    mov ebx, 2
    div ebx

    ; EDX stores remainder. If remainder is 0, number is even, otherwise number is odd.
    test edx, edx
    jne add_to_odd
    inc esi
    jmp test_end
add_to_odd:
    inc edi
test_end:
    loop next_element ; Decrement ecx, if not zero, go to next element.

    PRINTF32 `Num even is %u, num odd is %u\n\x0`, esi, edi

    ret
