# Writeup

- First use this command to scan the executable:
> ```Bash
> objdump -M intel -d break_this
> ```

- The `main()` function only calls `read_buffer()`.
- This function reads the length of a buffer from standard input into a variable `n`.
- Then it reads the buffer itself (`char buffer[64]`). Because `fgets()` reads at most `n - 1` characters, we can set `n` to a value bigger than the length of the buffer, so an overflow may be possible.
- We will set `n` to a large enough value: `128`

- `magic_function()` starts at address `0x08048596`
- From the first 4 lines from `read_buffer()` we get that: `ebp` and `edi` get pushed on the stack, then the stack is extended by `0x54` = `84`
- So we must print `88 + 4 + 4 = 92` dummy characters `A` and then the address of `magic_function()` in little-endian encoding

> ``` Bash
> python2 -c 'print "128\n" + "A"*92 + "\x96\x85\x04\x08"' > payload
> ```