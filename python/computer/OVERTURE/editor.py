import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os




def open_file():
    filepath = askopenfilename(
        filetypes=[("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")

def save_file():
    with open("assembly.ovt", "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - assembly.ovt")

def run_file():
    save_file()
    os.system("python assembler+interpreter.py")

window = tk.Tk()
window.title("Text Editor Application")

window.rowconfigure(0, minsize=900, weight=1)
window.columnconfigure(1, minsize=900, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save", command=save_file)
btn_run = tk.Button(fr_buttons, text="Run", command=run_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_run.grid(row=2, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()