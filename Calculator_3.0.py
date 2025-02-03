import tkinter as tk


res = None
operator = ''


def get_values():
    try:
        return int(number_entry.get())
    except ValueError:
        return 0


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, str(value))


def add():
    global res, operator
    operator = '+'
    res = get_values()
    number_entry.delete(0, 'end')


def sub():
    global res, operator
    operator = '-'
    res = get_values()
    number_entry.delete(0, 'end')


def div():
    global res, operator
    operator = '/'
    res = get_values()
    number_entry.delete(0, 'end')


def mul():
    global res, operator
    operator = '*'
    res = get_values()
    number_entry.delete(0, 'end')


def clear():
    global res, operator
    res = None
    operator = ''
    number_entry.delete(0, 'end')
    answer_entry.delete(0, 'end')


def calculate():
    global res, operator
    num2 = get_values()
    if res is None or operator == '':
        return
    try:
        if operator == "+":
            res += num2
        elif operator == "-":
            res -= num2
        elif operator == "*":
            res *= num2
        elif operator == "/":
            if num2 == 0:
                insert_values("Ошибка")
                return
            res /= num2
        insert_values(res)
        number_entry.delete(0, 'end')
    except Exception as e:
        insert_values("Ошибка")


def press_number(num):
    number_entry.insert('end', str(num))


window = tk.Tk()
window.title('Калькулятор')
window.geometry('200x330')
window.resizable(False, False)

button_ADD = tk.Button(window, text='+', width=4, height=2, command=add, background='grey', activebackground='grey')
button_ADD.place(x=20, y=80)
button_SUB = tk.Button(window, text='-', width=4, height=2, command=sub, background='grey', activebackground='grey')
button_SUB.place(x=20, y=120)
button_MUL = tk.Button(window, text='*', width=4, height=2, command=mul, background='grey', activebackground='grey')
button_MUL.place(x=20, y=160)
button_DIV = tk.Button(window, text='/', width=4, height=2, command=div, background='grey', activebackground='grey')
button_DIV.place(x=20, y=200)

button_CLEAR = tk.Button(window, text='C', width=4, height=2, command=clear)
button_CLEAR.place(x=60, y=200)
button_1 = tk.Button(window, text='1', width=4, height=2, command=lambda: press_number(1))
button_1.place(x=60, y=80)
button_2 = tk.Button(window, text='2', width=4, height=2, command=lambda: press_number(2))
button_2.place(x=100, y=80)
button_3 = tk.Button(window, text='3', width=4, height=2, command=lambda: press_number(3))
button_3.place(x=140, y=80)
button_4 = tk.Button(window, text='4', width=4, height=2, command=lambda: press_number(4))
button_4.place(x=60, y=120)
button_5 = tk.Button(window, text='5', width=4, height=2, command=lambda: press_number(5))
button_5.place(x=100, y=120)
button_6 = tk.Button(window, text='6', width=4, height=2, command=lambda: press_number(6))
button_6.place(x=140, y=120)
button_7 = tk.Button(window, text='7', width=4, height=2, command=lambda: press_number(7))
button_7.place(x=60, y=160)
button_8 = tk.Button(window, text='8', width=4, height=2, command=lambda: press_number(8))
button_8.place(x=100, y=160)
button_9 = tk.Button(window, text='9', width=4, height=2, command=lambda: press_number(9))
button_9.place(x=140, y=160)
button_0 = tk.Button(window, text='0', width=4, height=2, command=lambda: press_number(0))
button_0.place(x=100, y=200)
button_equal = tk.Button(window, text='=', width=4, height=2, command=calculate)
button_equal.place(x=140, y=200)

number_entry = tk.Entry(window, width=26)
number_entry.place(x=20, y=40)
answer_entry = tk.Entry(window, width=26)
answer_entry.place(x=20, y=280)

number_name = tk.Label(window, text='Введите число:')
number_name.place(x=20, y=10)
answer_name = tk.Label(window, text='Ответ:')
answer_name.place(x=20, y=250)

window.mainloop()