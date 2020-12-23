# Spiking

Create a .spk file for every cmd to spike

```
s_readline();
s_string("<cmd> ");
s_string_variable("A");
```

```Bash
generic_send_tcp <ip> <port> <spike script> 0 0
```
