import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class KeyLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Key Logger Viewer")
        self.root.geometry("500x400")

        self.text_box = ScrolledText(root, wrap=tk.WORD)
        self.text_box.pack(expand=True, fill="both")
        self.text_box.config(state=tk.DISABLED)
    def show_key(self, key_str):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, key_str+ "\n")
        self.text_box.yview(tk.END)
        self.text_box.config(state=tk.DISABLED)