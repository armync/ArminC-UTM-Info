%include "printf32.asm"

section .text
    global main
    extern printf

main:
    mov al, 0xFF
    PRINTF32 `CF nu e activ\n\x0`
    test al, al
    add al, 1
    jc carry_flag
    jmp end

carry_flag:
    PRINTF32 `CF activ\n\x0`

end:
    ret
