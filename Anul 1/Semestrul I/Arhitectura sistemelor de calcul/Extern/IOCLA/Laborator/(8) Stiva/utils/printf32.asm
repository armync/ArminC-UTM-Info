;;;;;;;;;;;;;;;;;;;;;;;;;;;;
%macro PRINTF32 1-*
	pushf
	pushad
 	jmp     %%endstr 
%%str:       db      %1 
%%endstr:
%rep  %0 - 1
%rotate -1
        push    dword %1 
%endrep
 	push %%str	
	call printf
	add esp, 4*%0
	popad
	popf
%endmacro
;;;;;;;;;;;;;;;;;;;;;;;;;;;;
