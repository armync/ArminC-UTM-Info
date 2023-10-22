; SPDX-License-Identifier: BSD-3-Clause

BITS 64
section .text

global get_max

get_max:
	push  rbp
	mov rbp, rsp

	push rbx ; the callee should save ebx if it uses it

	mov rbx, rdi ; first argument
	mov rcx, rsi ; second argument
	; third argument is in rdx

	xor rax, rax

compare:
	cmp eax, [rbx+rcx*4-4]
	jge check_end
	mov r12, rcx ; array starts at zero: use fancy 64-bit arch register
	dec r12
	mov [rdx], r12 ; save position
	mov eax, [rbx+rcx*4-4]
check_end:
	loopnz compare

	pop rbx ; the callee should restore ebx before returning
	leave
	ret
