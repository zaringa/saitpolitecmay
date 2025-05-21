from tkinter import *
from tkinter import filedialog

root = Tk("TextEditor")
text = Text(root)
text.grid()
root.title("Текстовый редактор на Python")
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    if savelocation: 
        with open(savelocation, "w+") as file1:
            file1.write(t)

button = Button(root, text="Save", command=saveas)
button.grid()

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

Helvetica = IntVar()
arial = IntVar()
times = IntVar()
Courier = IntVar()

font.menu.add_checkbutton(label="Courier", variable=Courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica, command=FontHelvetica)

# === доп. библиотеки ===

from tkinter import simpledialog

# --- Подсчет слов и символов ---
def update_stats(event=None):
    content = text.get("1.0", "end-1c")
    words = len(content.split())
    chars = len(content)
    root.title(f"Текстовый редактор на Python — Слова: {words} | Символы: {chars}")

text.bind("<KeyRelease>", update_stats)


# --- Поиск и подсветка слова ---
def search_word(event=None):
    text.tag_remove("found", "1.0", "end")
    word = simpledialog.askstring("Search", "Enter word to find:")
    if word:
        start = "1.0"
        while True:
            pos = text.search(word, start, stopindex="end")
            if not pos:
                break
            end = f"{pos}+{len(word)}c"
            text.tag_add("found", pos, end)
            start = end
        text.tag_config("found", background="yellow")



# --- Выход по Ctrl+Q ---
def quit_editor(event=None):
    root.quit()

# --- Привязка горячих клавиш ---
root.bind("<Control-f>", search_word)
root.bind("<Control-q>", quit_editor)


# --- Переключение темы ---
is_dark_mode = False

def toggle_theme():
    global is_dark_mode
    if not is_dark_mode:
        text.config(bg="#1e1e1e", fg="#dcdcdc", insertbackground="#ffffff")
        root.config(bg="#1e1e1e")
    else:
        text.config(bg="white", fg="black", insertbackground="black")
        root.config(bg="SystemButtonFace")
    is_dark_mode = not is_dark_mode

theme_button = Button(root, text="Сменить тему", command=toggle_theme)
theme_button.grid()

# --- Сохранение по Ctrl+S ---
def manual_save(event=None):
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    if savelocation:
        with open(savelocation, "w+", encoding="utf-8") as file1:
            file1.write(t)

root.bind("<Control-s>", manual_save)

root.mainloop()

