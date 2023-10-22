; SPDX-License-Identifier: BSD-3-Clause

extern printf

section .data
	message db "Hello", 0

section .text

global print_hello

print_hello:
	push ebp

	; leave este echivalent cu setul de instrucțiuni:
	; mov esp, ebp
	; pop ebp
	;
	; În absența acestei instrucțiuni (salvarea frame pointerului curent),
	; leave ar restaura vârful stivei (esp) la inceputul frame-ului precedent,
	; deasupra căruia, pe stivă, se află un ebp, urmat de adresa de return
	; a funcției din care a fost apelată print_hello(); astfel, la executarea
	; instrucțiunii ret de la finalul print_hello(), se va sări imediat după
	; apelul funcției asm_call_wrapper();
	mov ebp, esp

	push message
	call printf
	add esp, 4

	leave
	ret
