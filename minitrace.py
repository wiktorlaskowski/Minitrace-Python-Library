import sys
import traceback
from colorama import Fore, Style, init
from tkinter import Tk, filedialog

init(autoreset=True)

class MiniTrace:
    _trace_length = 5

    @classmethod
    def settracelengthto(cls, length):
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Trace length must be a positive integer.")
        cls._trace_length = length

    @classmethod
    def format_traceback(cls, exc_type, exc_value, tb):
        trace_lines = traceback.extract_tb(tb)[-cls._trace_length:]
        formatted_lines = []

        for idx, line in enumerate(reversed(trace_lines), 1):
            code_line = line.line.strip() if line.line else "No code found"
            if idx == 1:
                formatted_lines.append(f"{Fore.RED}{line.lineno} >>> {code_line}{Style.RESET_ALL}")
            else:
                formatted_lines.append(f"{line.lineno} >>> {code_line}")

        expectation = f"{Fore.RED}{exc_type.__name__}: {exc_value}{Style.RESET_ALL}"
        formatted_lines.append(expectation)
        formatted_traceback = "\n".join(formatted_lines)
        return f"Traceback: Most recent calls\n{formatted_traceback}"

    @classmethod
    def format_traceback_plain(cls, exc_type, exc_value, tb):
        trace_lines = traceback.extract_tb(tb)[-cls._trace_length:]
        formatted_lines = [
            f"{line.lineno} >>> {line.line.strip() if line.line else 'No code found'}"
            for line in reversed(trace_lines)
        ]
        expectation = f"{exc_type.__name__}: {exc_value}"
        return f"Traceback: Most recent calls\n" + "\n".join(formatted_lines)

    @classmethod
    def hook(cls):
        sys.excepthook = cls.handle_exception

    @classmethod
    def handle_exception(cls, exc_type, exc_value, tb):
        formatted_trace = cls.format_traceback(exc_type, exc_value, tb)
        print(formatted_trace, file=sys.stderr)
        try:
            response = input("Would you like to save this traceback to a file? (y/n): ").strip().lower()
            if response == "y":
                cls.save_to_file(exc_type, exc_value, tb)
        except KeyboardInterrupt:
            print("\nSave operation canceled due to KeyboardInterrupt.")

    @classmethod
    def save_to_file(cls, exc_type, exc_value, tb):
        plain_traceback = cls.format_traceback_plain(exc_type, exc_value, tb)
        Tk().withdraw()
        file_path = filedialog.asksaveasfilename(
            defaultextension=".log",
            filetypes=[("Log files", "*.log"), ("Text files", "*.txt"), ("No extension iles", ".")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(plain_traceback)
            print(f"Traceback saved to {file_path}")
        else:
            print("Save operation canceled.")
