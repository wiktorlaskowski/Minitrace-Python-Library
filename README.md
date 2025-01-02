![minitrace_light](https://github.com/user-attachments/assets/8033396d-e759-4df6-ba4c-d14a493b4be5)
# Minitrace Python Library
Shorten those verbose Python tracebacks to something more compact, comes with saving!

Ever seen thove __long__ tracebacks? Welp, this is for you!
There are requirements:
# REQUIREMENTS
- __Colorama__ colorcodes the line with the error.
- __Tkinter__ for the file dialouge, probably installed but best to check.
# SETUP
1. First import the library. ___DO NOT USE `import minitrace` USE `from minitrace import MiniTrace`___
2. Hook to activate the library using `MiniTrace.hook()`
# `Full script`:
   ```Python
   from minitrace import MiniTrace
   MiniTrace.hook()
   ```
# HOW TO CUSTOMIZE
Use `MiniTrace.settracelengthto()` to set the length
### Example:
```Python
MiniTrace.settracelengthto(10)
```
# NOTES:
Pip does not support minitrace, you will need to download the file from raw code to activate it.
