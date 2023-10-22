; SPDX-License-Identifier: BSD-3-Clause

extern printf
extern double_array

section .data
	myarray dd 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
	myarray_len dd 10

	format_string db "%d ", 0
	newline db 13, 10, 0


section .text


print_reverse_array:
	push ebp
	mov ebp, esp

	; save ebx in callee
	push ebx

	; [ebp+8] is array pointer
	; [ebp+12] is array length
	mov ebx, [ebp+8]
	mov ecx, [ebp+12]
	xor eax, eax

next:

;   TODO1: Decomentați următoarele două linii comentate
    push ecx
	push dword [ebx+ecx*4-4]
	push format_string
	call printf
	add esp, 8
    pop ecx
	loop next

	push newline
	call printf
	add esp, 4

	pop ebx

	leave
	ret


global main

main:
	push ebp
	mov ebp, esp

	mov edx, [myarray_len]
	lea eax, [myarray]

;   TODO2: Decomentați această secvență de cod
    push edx
    push eax
    call double_array
    add esp, 8

	mov edx, [myarray_len]
	lea eax, [myarray]
	push edx
	push eax
	call print_reverse_array
	add esp, 8


	leave
	ret
