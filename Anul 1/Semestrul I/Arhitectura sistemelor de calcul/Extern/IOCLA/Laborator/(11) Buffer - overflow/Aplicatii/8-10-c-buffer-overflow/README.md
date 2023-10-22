# Writeup

In `do_overflow.asm`:
   - `line 32` -> `sexy_var` is at `ebp-16`
   - `line 41` -> start reading buffer at `ebp-89`
   - 89 - 16 = 73 of `'A'`s
   - and `0x5541494D` written in little-endian encoding

For exercise 9, when running `objdump` in `main()`, look carefully at the instructions at the addresses `650` and `74b`, as well as the code around them.