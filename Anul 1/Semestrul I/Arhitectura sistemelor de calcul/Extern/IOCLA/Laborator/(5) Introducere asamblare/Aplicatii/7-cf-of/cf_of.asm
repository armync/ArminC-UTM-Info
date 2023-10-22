%include "printf32.asm"

section .text
    global main
    extern printf

main:

    mov al, 128
    PRINTF32 `CF si OF nu sunt active\n\x0`
    test al, al

    ; Orice valoare intre 128 si 255 va activa CF si OF
    add al, 128

    jc cf_on
    jmp end

cf_on:
    jo cf_of_on
    jmp end

cf_of_on:
    PRINTF32 `CF si OF activ\n\x0`

end:
    ret

