import os
import sys
import traceback
from colorama import Fore, Style, init
from tkinter import Tk, filedialog

init(autoreset=True)

class MiniTrace:
    _trace_length = 5
    _show_full_path = False
    _auto_save = False
    _auto_save_path = None

    @classmethod
    def settracelengthto(cls, length):
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Trace length must be a positive integer.")
        cls._trace_length = length

    @classmethod
    def set_show_full_path(cls, show):
        cls._show_full_path = bool(show)

    @classmethod
    def enable_auto_save(cls, path=None):
        cls._auto_save = True
        cls._auto_save_path = path

    @classmethod
    def disable_auto_save(cls):
        cls._auto_save = False
        cls._auto_save_path = None

    @classmethod
    def format_traceback(cls, exc_type, exc_value, tb):
        trace_lines = traceback.extract_tb(tb)[-cls._trace_length:]
        formatted_lines = []

        for idx, line in enumerate(reversed(trace_lines), 1):
            code_line = line.line.strip() if line.line else "No code found"
            filename = line.filename if cls._show_full_path else os.path.basename(line.filename)
            info = f"{filename}:{line.lineno}"
            if idx == 1:
                formatted_lines.append(f"{Fore.RED}{info} >>> {code_line}{Style.RESET_ALL}")
            else:
                formatted_lines.append(f"{info} >>> {code_line}")

        expectation = f"{Fore.RED}{exc_type.__name__}: {exc_value}{Style.RESET_ALL}"
        formatted_lines.append(expectation)
        formatted_traceback = "\n".join(formatted_lines)
        return f"Traceback: Most recent calls\n{formatted_traceback}"

    @classmethod
    def format_traceback_plain(cls, exc_type, exc_value, tb):
        trace_lines = traceback.extract_tb(tb)[-cls._trace_length:]
        formatted_lines = []
        for line in reversed(trace_lines):
            code_line = line.line.strip() if line.line else 'No code found'
            filename = line.filename if cls._show_full_path else os.path.basename(line.filename)
            info = f"{filename}:{line.lineno}"
            formatted_lines.append(f"{info} >>> {code_line}")
        expectation = f"{exc_type.__name__}: {exc_value}"
        formatted_lines.append(expectation)
        return (
            "Traceback: Most recent calls\n" + "\n".join(formatted_lines)
        )

    @classmethod
    def init(cls):
        sys.excepthook = cls.handle_exception

    @classmethod
    def handle_exception(cls, exc_type, exc_value, tb):
        formatted_trace = cls.format_traceback(exc_type, exc_value, tb)
        print(formatted_trace, file=sys.stderr)
        try:
            if cls._auto_save:
                cls.save_to_file(exc_type, exc_value, tb, cls._auto_save_path)
            else:
                response = input("Would you like to save this traceback to a file? (y/n): ").strip().lower()
                if response == "y":
                    cls.save_to_file(exc_type, exc_value, tb)
        except KeyboardInterrupt:
            print("\nSave operation canceled due to KeyboardInterrupt.")

    @classmethod
    def save_to_file(cls, exc_type, exc_value, tb, path=None):
        plain_traceback = cls.format_traceback_plain(exc_type, exc_value, tb)
        if path is None:
            Tk().withdraw()
            path = filedialog.asksaveasfilename(
                defaultextension=".log",
                filetypes=[
                    ("Log files", "*.log"),
                    ("Text files", "*.txt"),
                    ("All files", "*.*"),
                ]
            )
        if path:
            with open(path, "w") as file:
                file.write(plain_traceback)
            print(f"Traceback saved to {path}")
        else:
            print("Save operation canceled.")
