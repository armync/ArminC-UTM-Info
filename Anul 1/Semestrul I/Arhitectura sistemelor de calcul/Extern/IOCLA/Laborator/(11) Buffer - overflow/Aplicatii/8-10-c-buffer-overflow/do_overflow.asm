	.file	"do_overflow.c"
	.intel_syntax noprefix
	.section	.rodata
.LC0:
	.string	"insert buffer string: "
.LC1:
	.string	"buffer is: "
.LC2:
	.string	" %02X(%c)"
.LC3:
	.string	""
.LC4:
	.string	"Full of win!"
.LC5:
	.string	"Not quite there. Try again!"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	lea	ecx, [esp+4]
	.cfi_def_cfa 1, 0
	and	esp, -16
	push	DWORD PTR [ecx-4]
	push	ebp
	.cfi_escape 0x10,0x5,0x2,0x75,0
	mov	ebp, esp
	push	ecx
	.cfi_escape 0xf,0x3,0x75,0x7c,0x6
	sub	esp, 100
	mov	DWORD PTR [ebp-16], -17958194
	sub	esp, 12
	push	OFFSET FLAT:.LC0
	call	printf
	add	esp, 16
	mov	eax, DWORD PTR stdin
	sub	esp, 4
	push	eax
	push	128
	lea	eax, [ebp-89]
	push	eax
	call	fgets
	add	esp, 16
	sub	esp, 12
	push	OFFSET FLAT:.LC1
	call	printf
	add	esp, 16
	sub	esp, 12
	lea	eax, [ebp-89]
	push	eax
	call	strlen
	add	esp, 16
	mov	DWORD PTR [ebp-20], eax
	mov	DWORD PTR [ebp-12], 0
	jmp	.L2
.L3:
	lea	edx, [ebp-89]
	mov	eax, DWORD PTR [ebp-12]
	add	eax, edx
	movzx	eax, BYTE PTR [eax]
	movsx	edx, al
	lea	ecx, [ebp-89]
	mov	eax, DWORD PTR [ebp-12]
	add	eax, ecx
	movzx	eax, BYTE PTR [eax]
	movsx	eax, al
	sub	esp, 4
	push	edx
	push	eax
	push	OFFSET FLAT:.LC2
	call	printf
	add	esp, 16
	add	DWORD PTR [ebp-12], 1
.L2:
	mov	eax, DWORD PTR [ebp-12]
	cmp	eax, DWORD PTR [ebp-20]
	jb	.L3
	sub	esp, 12
	push	OFFSET FLAT:.LC3
	call	puts
	add	esp, 16
	movzx	eax, BYTE PTR [ebp-84]
	mov	BYTE PTR [ebp-22], al
	cmp	DWORD PTR [ebp-16], 1430341965
	jne	.L4
	sub	esp, 12
	push	OFFSET FLAT:.LC4
	call	puts
	add	esp, 16
	jmp	.L5
.L4:
	sub	esp, 12
	push	OFFSET FLAT:.LC5
	call	puts
	add	esp, 16
.L5:
	mov	eax, 0
	mov	ecx, DWORD PTR [ebp-4]
	.cfi_def_cfa 1, 0
	leave
	.cfi_restore 5
	lea	esp, [ecx-4]
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
