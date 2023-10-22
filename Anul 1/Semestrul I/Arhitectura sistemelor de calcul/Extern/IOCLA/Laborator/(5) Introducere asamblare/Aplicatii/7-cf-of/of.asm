%include "printf32.asm"

section .text
    global main
    extern printf

main:

    mov al, 0x7F
    PRINTF32 `OF nu e activ\n\x0`
    test al, al
    add al, 1
    jo overflow_flag
    jmp end

overflow_flag:
    PRINTF32 `OF activ\n\x0`

end:
    ret
