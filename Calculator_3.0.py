import tkinter as tk
from tkinter import ttk


res = None
operator = ''
input_text = ''


def press_num(num):
    global input_text
    if len(input_text) < 13:
        input_text += str(num)
        update_display(input_text)


def update_display(value):
    number_entry.delete(0, 'end')
    number_entry.insert('end', value)


def add():
    global res, operator, input_text
    if input_text:
        res = float(input_text)
        operator = '+'
        input_text = ''
        update_display(res)


def sub():
    global res, operator, input_text
    if input_text:
        res = float(input_text)
        operator = '-'
        input_text = ''
        update_display(res)


def div():
    global res, operator, input_text
    if input_text:
        res = float(input_text)
        operator = '/'
        input_text = ''
        update_display(res)


def mul():
    global res, operator, input_text
    if input_text:
        res = float(input_text)
        operator = '*'
        input_text = ''
        update_display(res)


def clear():
    global res, operator, input_text
    res = None
    operator = ''
    input_text = ''
    update_display('')


def backspace():
    global input_text
    input_text = input_text[:-1]
    update_display(input_text)


def percent():
    global input_text
    if input_text:
        try:
            input_text = str(float(input_text) / 100)
            update_display(input_text)
        except ValueError:
            update_display('Ошибка')

def memory():
    global input_text
    pass


def calculate():
    global res, operator, input_text
    if input_text and res is not None:
        try:
            num2 = float(input_text)
            if operator == '+':
                res += num2
            elif operator == '-':
                res -= num2
            elif operator == '*':
                res *= num2
            elif operator == '/':
                if num2 == 0:
                    update_display('Ошибка')
                    return
                res /= num2
            input_text= str(res)
            update_display(input_text)
        except Exception as e:
            update_display('Ошибка')


window = tk.Tk()
window.title('Калькулятор')
window.geometry('400x600')
window.resizable(False, False)
window.configure(bg='black')

number_entry = tk.Entry(window, width=15, justify='right', font=('Avenir Next Cyr Thin', 30), bd=0, bg='black', fg='white')
number_entry.place(x=10, y=20)

separator = tk.Canvas(window, width=400, height=1, bg='white', highlightthickness=0)
separator.place(x=0, y=98)

buttons = [
    ('C', 0, 100, clear),
    ('CE', 100, 100, backspace),
    ('%', 200, 100, percent),
    ('/', 300, 100, div),
    ('7', 0, 200, lambda: press_num(7)),
    ('8', 100, 200, lambda: press_num(8)),
    ('9', 200, 200, lambda: press_num(9)),
    ('*', 300, 200, mul),
    ('4', 0, 300, lambda: press_num(4)),
    ('5', 100, 300, lambda: press_num(5)),
    ('6', 200, 300, lambda: press_num(6)),
    ('-', 300, 300, sub),
    ('1', 0, 400, lambda: press_num(1)),
    ('2', 100, 400, lambda: press_num(2)),
    ('3', 200, 400, lambda: press_num(3)),
    ('+', 300, 400, add),
    ('MR', 0, 500, memory),
    ('0', 100, 500, lambda: press_num(0)),
    ('.', 200, 500, lambda: press_num('.')),
    ('=', 300, 500, calculate)
]

style = ttk.Style()
style.theme_use('clam')
style.configure('Rounded.TButton',
                font=('Avenir Next Cyr Thin', 30),
                background='#000000',  # Не работает в ttk, но поможет для системных тем
                foreground='white',
                borderwidth=1,
                padding=10,
                relief='flat')

style.map('Rounded.TButton',
          background=[('active', '#222222')],
          foreground=[('active', 'white')])

for text, x, y, command in buttons:
    ttk.Button(window, text=text, style='Rounded.TButton', command=command).place(x=x, y=y, width=100, height=100)

window.mainloop()