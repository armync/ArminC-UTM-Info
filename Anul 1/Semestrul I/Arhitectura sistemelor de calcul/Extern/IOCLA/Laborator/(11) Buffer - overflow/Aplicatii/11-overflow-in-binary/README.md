# Writeup

   - We can use Ghidra to disassemble the exec.
   - The number of arguments given to the `main()` function must be equal to 2 (one is the name of the executable file).
   - The second argument (the one given to the executable in the command line) is passed to the function `check_string()`.

In `check_string()`:
   - `local_10` must be set to `0x4E305250` to call `success()` (carefully, use the little-endian encoding)
   - `local_10` is stored at stack - `0x10`
   - The buffer is stored at `stack - 0x30`
   - So the payload should consist of `32 (48 - 16)` `'A'` characters, followed by `"\x50\x52\x30\x4E"`