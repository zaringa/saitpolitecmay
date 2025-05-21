**Техническая документация**  
**Текстовый редактор на Python с использованием Tkinter**  
*Версия 1.0*  

###Московский политех 

---

### **1. Спецификация документа**

| **Параметр**       | **Значение**                |
|---------------------|-----------------------------|
| Версия ПО           | 1.0                         |
| Язык программирования | Python 3.10+               |
| Зависимости         | tkinter (стандартная библиотека) |
| Автор               | [Ваше имя/название компании] |
| Дата публикации     | [Дата]                      |

---

### **2. Оглавление**  
1. Введение  
2. Системные требования  
3. Установка и настройка  
4. Архитектура решения  
5. Руководство разработчика  
6. Тестирование  
7. Справочные материалы  

---

### **3. Введение**  
**3.1 Назначение**  
Документ описывает процесс разработки текстового редактора с графическим интерфейсом на базе библиотеки Tkinter.

**3.2 Область применения**  
Решение предназначено для:  
✓ Образовательных целей  
✓ Быстрого редактирования текстовых файлов  
✓ Демонстрации возможностей Python GUI  

---

### **4. Системные требования**  
**4.1 Аппаратные:**  
- Процессор: x86, 1 ГГц  
- ОЗУ: 512 МБ  
- Дисковое пространство: 5 МБ  

**4.2 Программные:**  
- ОС: Windows 7+/Linux/macOS  
- Python 3.10+  
- Библиотека tkinter  

---

### **5. Установка**  
**5.1 Пошаговая инструкция:**  
1. Установите Python с официального сайта  
2. Проверьте установку tkinter:  
   ```bash
   python -m tkinter
   ```
3. Скопируйте код приложения (Приложение A)  
4. Запустите файл:  
   ```bash
   python text_editor.py
   ```

---

### **6. Архитектура**  
**6.1 Блок-схема:**  
graph TD
    A[Запуск приложения] --> B[Создание главного окна]
    B --> C[Инициализация виджетов]
    C --> D[Текстовое поле]
    C --> E[Кнопка Save]
    C --> F[Меню шрифтов]
    C --> G[Кнопка темы]

    E --> H[Функция saveas]
    H --> I[Диалог сохранения файла]
    I --> J[Запись в файл]

    F --> K[Выбор шрифта]
    K --> L[FontHelvetica]
    K --> M[FontCourier]

    G --> N[Функция toggle_theme]
    N --> O[Переключение цветовой схемы]

    D --> P[Обработка ввода]
    P --> Q[Функция update_stats]
    Q --> R[Подсчет слов/символов]
    Q --> S[Обновление заголовка]

    T[Горячие клавиши] --> U[Ctrl+S: Сохранение]
    T --> V[Ctrl+F: Поиск]
    T --> W[Ctrl+Q: Выход]

    V --> X[Функция search_word]
    X --> Y[Диалог поиска]
    Y --> Z[Подсветка результатов]

    style A fill:#4CAF50,stroke:#388E3C
    style H fill:#2196F3,stroke:#1976D2
    style N fill:#9C27B0,stroke:#6A1B9A
    style Q fill:#FF9800,stroke:#F57C00
    style X fill:#E91E63,stroke:#C2185B

**6.2 Компоненты:**  
- Главное окно (MainWindow)  
- Текстовое поле (TextWidget)  
- Панель инструментов (Toolbar)  
- Меню (MainMenu)  

---

### **7. Руководство разработчика**  
**7.1 Основные функции:**  
```python
# Создание главного окна
root = Tk()
root.title("Text Editor v1.0")

# Инициализация текстового поля
text_area = Text(root, wrap=WORD)
text_area.pack(expand=True, fill=BOTH)
```

**7.2 Обработка событий:**  
```python
# Привязка горячих клавиш
root.bind("<Control-s>", lambda e: save_file())
```

---

### **8. Тестирование**  
**8.1 Тест-кейсы:**  

| №  | Действие               | Ожидаемый результат        |
|----|------------------------|----------------------------|
| 1  | Нажатие Ctrl+S         | Открытие диалога сохранения |
| 2  | Ввод текста            | Автообновление статистики  |

---

### **9. Приложения**  

**Приложение А. Горячие клавиши**  
- Ctrl+S: Сохранить  
- Ctrl+F: Поиск  
- Ctrl+Q: Выход  

##Приведу подробное пошаговое руководство по созданию этого текстового редактора:

---

## Шаг 1: Базовая настройка окна
```python
from tkinter import *
from tkinter import filedialog

root = Tk("TextEditor")
root.title("Текстовый редактор на Python")
text = Text(root)
text.grid()
```
Объяснение:
- Импорт библиотек Tkinter
- Создание главного окна с названием
- Добавление текстового поля и его размещение

## Шаг 2: Система сохранения файлов
```python
def saveas():
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    if savelocation: 
        with open(savelocation, "w+") as file1:
            file1.write(t)

button = Button(root, text="Save", command=saveas)
button.grid()
```
Особенности:
- `end-1c` исключает последний символ переноса строки
- Диалоговое окно выбора места сохранения
- Кнопка для вызова функции

## Шаг 3: Меню выбора шрифтов
```python
def FontHelvetica():
    text.config(font="Helvetica")

def FontCourier():
    text.config(font="Courier")

font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

font.menu.add_checkbutton(label="Courier", command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", command=FontHelvetica)
```
Важно:
- Использование MenuButton вместо стандартного Menu
- Checkbuttons для выбора шрифтов
- Динамическое изменение конфигурации текстового поля

## Шаг 4: Статистика текста
```python
def update_stats(event=None):
    content = text.get("1.0", "end-1c")
    words = len(content.split())
    chars = len(content)
    root.title(f"Слова: {words} | Символы: {chars}")

text.bind("<KeyRelease>", update_stats)
```
Примечания:
- Обновление статистики при каждом нажатии клавиши
- Отображение в заголовке окна
- `split()` для подсчета слов (упрощенный метод)

## Шаг 5: Поиск с подсветкой
```python
def search_word():
    text.tag_remove("found", "1.0", "end")
    word = simpledialog.askstring("Search", "Enter word:")
    if word:
        start = "1.0"
        while True:
            pos = text.search(word, start, stopindex="end")
            if not pos: break
            end = f"{pos}+{len(word)}c"
            text.tag_add("found", pos, end)
            start = end
        text.tag_config("found", background="yellow")

root.bind("<Control-f>", search_word)
```
Особенности:
- Использование тегов для подсветки
- Цикличный поиск всех вхождений
- Горячая клавиша Ctrl+F

## Шаг 6: Темная тема
```python
is_dark_mode = False

def toggle_theme():
    global is_dark_mode
    colors = {
        False: {"bg": "white", "fg": "black"},
        True: {"bg": "#1e1e1e", "fg": "#dcdcdc"}
    }
    text.config(**colors[is_dark_mode])
    root.config(bg=colors[is_dark_mode]["bg"])
    is_dark_mode = not is_dark_mode

theme_button = Button(root, text="Тема", command=toggle_theme)
theme_button.grid()
```

## Шаг 7: Горячие клавиши
```python
def quit_editor(event=None):
    root.quit()

root.bind("<Control-s>", lambda e: saveas())
root.bind("<Control-q>", quit_editor)
```
Доступные комбинации:
- Ctrl+S: Сохранить
- Ctrl+F: Поиск
- Ctrl+Q: Выход

## Шаг 8: Запуск приложения
```python
root.mainloop()
```

---

### Советы для улучшения:
1. Добавьте функцию открытия файлов:
```python
def open_file():
    file = filedialog.askopenfile()
    text.insert(INSERT, file.read())
```

2. Исправьте подсчет слов:
```python
import re
words = len(re.findall(r'\w+', content))
```

3. Добавьте поддержку других шрифтов:
```python
font.menu.add_checkbutton(label="Arial", command=lambda: text.config(font="Arial"))
```

4. Реализуйте систему уведомлений:
```python
from tkinter import messagebox
messagebox.showinfo("Сохранено", "Файл успешно сохранен!")
```

Полный код можно найти в оригинальном сообщении. Для запуска просто сохраните код как `text_editor.py` и выполните:
```bash
python text_editor.py
```