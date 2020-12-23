# Fuzzing

1. Find where the app crashes
2. Fuzz again with base = 1 increment before the crash
3. Use larger increments per crash to try and overwrite the ESP and ultimately the EIP
