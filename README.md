![minitrace_light](https://github.com/user-attachments/assets/8033396d-e759-4df6-ba4c-d14a493b4be5)
# Minitrace Python Library
Shorten those verbose Python tracebacks to something more compact, comes with saving!

Ever seen those **long** tracebacks? Well, this is for you!
# REQUIREMENTS
- __Colorama__ colorcodes the line with the error.
- __Tkinter__ for the file dialogue, probably installed but best to check.
# MAIN WEBSITE
Go to the website at https://wiktorlaskowski.github.io/Minitrace-Python-Library/
# SETUP
1. First import the library. ___DO NOT USE `import minitrace` USE `from minitrace import MiniTrace`___
2. Initialize the library using the init function
   `MiniTrace.init()`
# `Full script`:
   ```Python
   from minitrace import MiniTrace
   MiniTrace.init()
   ```
# HOW TO CUSTOMIZE
Use `MiniTrace.settracelengthto()` to set the length
### Example:
```Python
MiniTrace.settracelengthto(10)
```
# NOTES:
Pip does not support minitrace, you will need to download the file from raw code to activate it.
