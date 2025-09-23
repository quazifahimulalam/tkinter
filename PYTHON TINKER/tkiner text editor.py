import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser, font
from tkinter.scrolledtext import ScrolledText

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("untitled - Text Editor")
        self.filename = None

        self.current_font_family = "consolas"
        self.current_font_size = 14
        self.text_font = font.Font(family=self.current_font_family, size=self.current_font_size)

        # text area with scrollebar
        self.text_area = ScrolledText(root, wrap="word", font=self.text_font, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.focus_set()

        # status bar
        self.status_bar = tk.Label(root, text="Ln 1, Col 1 ", anchor="e")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_area.bind("<KeyRelease>", self.update_status)
        self.text_area.bind("<ButtonRelease>", self.update_status)

        # menu bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # file menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: self.text_area.event_generate("<Cut>"))
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: self.text_area.event_generate("<Copy>"))
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: self.text_area.event_generate("<Paste>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", accelerator="Ctrl+F", command=self.find_text)
        edit_menu.add_command(label="Replace", accelerator="Ctrl+H", command=self.replace_text)

        # format menu
        format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Font", command=self.choose_font)
        format_menu.add_command(label="Text Color", command=self.choose_text_color)
        format_menu.add_command(label="Background Color", command=self.choose_bg_color)

        # help menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "text editor\nbuilt with tkinter"))

        # keaboard shortcuts
        root.bind("<Control-n>", lambda e: self.new_file())
        root.bind("<Control-o>", lambda e: self.open_file())
        root.bind("<Control-s>", lambda e: self.save_file())
        root.bind("<Control-f>", lambda e: self.find_text())
        root.bind("<Control-h>", lambda e: self.replace_text())

    # file operator
    def new_file(self):
        self.filename = None
        self.root.title("untitled - Text Editor")
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file:
            self.filename = file
            self.root.title(f"{file} - Text Editor")
            with open(file, "r") as f:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, f.read())

    def save_file(self):
        if not self.filename:
            self.save_as()
        else:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{self.filename} - Text Editor")

    def save_as(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text documents", "*.txt"), ("All Files", "*.*")])
        if file:
            self.filename = file
            self.save_file()

    # find and replace
    def find_text(self):
        word = simpledialog.askstring("Find", "Enter word:")
        if word:
            start = "1.0"
            while True:
                pos = self.text_area.search(word, start, stopindex=tk.END)
                if not pos:
                    break
                end = f"{pos}+{len(word)}c"
                self.text_area.tag_add("highlight", pos, end)
                self.text_area.tag_config("highlight", background="yellow", foreground="black")
                start = end

    def replace_text(self):
        find_word = simpledialog.askstring("Replace", "Enter word to find:")
        replace_word = simpledialog.askstring("Replace", "Enter word to replace with:")
        if find_word and replace_word:
            content = self.text_area.get(1.0, tk.END)
            new_content = content.replace(find_word, replace_word)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, new_content)

    # font and color
    def choose_font(self):
        font_family = simpledialog.askstring("font", "enter font family(e.g., Arial, Times New Roman, Courier New):")
        font_size = simpledialog.askinteger("font size", "enter font size:", initialvalue=self.current_font_size)
        if font_family and font_size:
            self.current_font_family = font_family
            self.current_font_size = font_size
            self.text_font.config(family=self.current_font_family, size=self.current_font_size)
            self.text_area.config(font=self.text_font)

    def choose_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

    def choose_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            try:
                start, end = self.text_area.index("sel.first"), self.text_area.index("sel.last")
                self.text_area.tag_add("highlight_bg", start, end)
                self.text_area.tag_config("highlight_bg", background=color)
            except tk.TclError:
                pass

    # status bar update
    def update_status(self, event=None):
        row, col = self.text_area.index(tk.INSERT).split(".")
        self.status_bar.config(text=f"Ln {row}, Col {int(col) + 1}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.geometry("800x600")
    root.mainloop()
