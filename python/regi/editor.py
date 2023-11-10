import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re

def open_file():
    global filepath
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
    global filepath
    if filepath is None:
        filepath = askopenfilename(
        filetypes=[("All Files", "*.*")]
        )
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")

def compile_file():
    save_file()
    os.system("python hcompiler.py")

def assemble_file():
    save_file()
    os.system("python assemblerimport.py")

def run_file():
    save_file()
    os.system("python high2py.py")
    os.system("python py.py")

window = tk.Tk()
window.title("Text Editor Application")

window.rowconfigure(0, minsize=900, weight=1)
window.columnconfigure(1, minsize=900, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save", command=save_file)
btn_compile = tk.Button(fr_buttons, text="Compile", command=compile_file)
btn_assemble = tk.Button(fr_buttons, text="Assemble", command=assemble_file)
btn_run = tk.Button(fr_buttons, text="Run", command=run_file)


btn_open.grid(row=0, column=0, sticky="ew", padx=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_compile.grid(row=2, column=0, sticky="ew", padx=5)
btn_assemble.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_run.grid(row=4, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

KEYWORD   = r"\b(?P<KEYWORD>[;].+)\b"
EXCEPTION = r"\b(?P<EXCEPTION>import)\b"        #import
BUILTIN   = r"\b(?P<BUILTIN>0b|0d|0x)"          #0d 0x 0b
DOCSTRING = r"\b(?P<DOCSTRING>[0-9a-f]+)\b"     #hexadecimale getallen
STRING    = r"\b(?<! )(?P<STRING>[a-z]+)\b"       #eerste woord
TYPES     = r"\b(?P<TYPES>const|label)\b" #const en label
NUMBER    = r"\b(?P<NUMBER>((0x|0b|0o|#)[\da-fA-F]+)|((\d*\.)?\d+))\b"
CLASSDEF  = r"(?<=\bclass)[ \t]+(?P<CLASSDEF>\w+)[ \t]*[:\(]" #recolor of DEFINITION for class definitions
DECORATOR = r"(^[ \t]*(?P<DECORATOR>@[\w\d\.]+))"
INSTANCE  = r"\b(?P<INSTANCE>super|self|cls)\b"
COMMENT   = r"(?P<COMMENT>#[^\n]*)"
SYNC      = r"(?P<SYNC>\n)"
PROG   = rf"{KEYWORD}|{TYPES}|{STRING}|{EXCEPTION}|{COMMENT}|{BUILTIN}|{DOCSTRING}|{SYNC}|{INSTANCE}|{DECORATOR}|{NUMBER}|{CLASSDEF}"
IDPROG = r"(?<!class)\s+(\w+)"

TAGDEFS   = {   #'COMMENT'    : {'foreground': CHARBLUE  , 'background': None},
                'TYPES'      : {'foreground': "00FF00"    , 'background': None},
                #'NUMBER'     : {'foreground': LEMON     , 'background': None},
                'BUILTIN'    : {'foreground': "#FFF000"  , 'background': None},
                'STRING'     : {'foreground': "#0000FF"  , 'background': None},
                'DOCSTRING'  : {'foreground': "#000FF0"  , 'background': None},
                'EXCEPTION'  : {'foreground': "#FFF000"   , 'background': None},
                #'DEFINITION' : {'foreground': SAILOR    , 'background': None},
                #'DECORATOR'  : {'foreground': CLOUD2    , 'background': None},
                #'INSTANCE'   : {'foreground': CLOUD     , 'background': None},
                'KEYWORD'    : {'foreground': "#F00000"  , 'background': None}
                #'CLASSDEF'   : {'foreground': PURPLE    , 'background': None}
            }

cd         = ic.ColorDelegator()
cd.prog    = re.compile(PROG, re.S|re.M)
cd.idprog  = re.compile(IDPROG, re.S)
cd.tagdefs = {**cd.tagdefs, **TAGDEFS}
ip.Percolator(txt_edit).insertfilter(cd)

filepath = None
window.mainloop()