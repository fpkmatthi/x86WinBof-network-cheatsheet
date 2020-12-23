# Offset

Create pattern for buffersize which can overwrite the EIP

```Bash
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <buffer size>
```

Put the output as the buffer and crash the app again

```Python
buffer=b'<pattern>'
```

Note the **EIP** value and get exact offset

```Bash
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l <buffer size> -q <EIP>
```

To verify, crash the app again with the following buffer:

```Pytho
buffer=b'A' * <offset> + b'B' * 4
```

The EIP should now contain **42424242** (42 = HEX value of B)
