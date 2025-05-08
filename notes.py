import tkinter as tk
from tkinter import font, colorchooser, simpledialog, messagebox

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Заміточки")

        self.text = tk.Text(root, wrap="word", font=("Arial", 12))
        self.text.pack(expand=True, fill="both")

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Очистити", command=self.clear_text)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=root.quit)

        format_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Формат", menu=format_menu)
        format_menu.add_command(label="Змінити шрифт", command=self.change_font)
        format_menu.add_command(label="Змінити фон", command=self.change_bg_color)

    def clear_text(self):
        self.text.delete("1.0", tk.END)

    def change_font(self):
        font_name = simpledialog.askstring("Шрифт", "Введіть назву шрифту (наприклад, Arial):")
        font_size = simpledialog.askinteger("Розмір", "Введіть розмір шрифту:")
        if font_name and font_size:
            try:
                self.text.config(font=(font_name, font_size))
            except tk.TclError:
                messagebox.showerror("Помилка", "Неправильний шрифт або розмір!")

    def change_bg_color(self):
        color = colorchooser.askcolor(title="Виберіть колір фону")[1]
        if color:
            self.text.config(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop() 
