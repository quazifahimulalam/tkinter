import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog,colorchooser,font
from tkinter.scrolledtext import ScrolledText

class TextEditor:
    def __init__(self,root):
        self.root =root
        self.root.title("untitled - Text Editor")
        self.filename = None
        
        self.current_font_family = "consolas"
        self.current_font_size = 14
        self.text_font = font.Font(family=self.current_font_family, size=self.current_font_size)
        
        # text area with scrollebar
        self.text_area = ScrolledText(root, wrap="word", font=self.text_font, undo=True)
        self.text_area.focus_set()
        
        #status bar
        self.status_bar = tk.Label(root, text="Ln 1, Col 1 ", anchor="e")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_area.bind("<KeyRelease>", self.update_status)
        self.text_area.bind("<ButtonRelease>", self.update_status)
        
        #menu bar
        self.menu_bar = tk.Menu(root)