# calculator_operations.py
import math
import tkinter.messagebox as messagebox

def append_to_display(display, char):
    current = display.get()
    if char in '+-*/':
        if current and current[-1] in '+-*/':
            display.delete(len(current)-1, tk.END)
    display.insert(tk.END, char)

def clear_display(display):
    display.delete(0, tk.END)

def delete_last_char(display):
    display.delete(len(display.get())-1, tk.END)

def toggle_sign(display):
    current = display.get()
    if current:
        try:
            if '(' in current or ')' in current:
                display.insert(tk.END, '-')
            elif current[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
        except:
            display.insert(tk.END, '-')

def calculate_square_root(display):
    try:
        current = display.get()
        if current:
            number = float(current)
            if number >= 0:
                result = math.sqrt(number)
                clear_display(display)
                display.insert(0, str(result))
            else:
                messagebox.showerror("错误", "不能对负数开平方根")
    except Exception as e:
        messagebox.showerror("错误", "无效的输入")
        clear_display(display)

def calculate_percentage(display):
    try:
        expression = display.get()
        if '%' in expression:
            parts = expression.split('%')
            if len(parts) == 2 and parts[1] == '':
                value = float(parts[0]) / 100
                clear_display(display)
                display.insert(0, str(value))
            else:
                before_percent = parts[0]
                after_percent = parts[1] if len(parts) > 1 else ''
                percent_value = eval(before_percent) / 100
                if after_percent:
                    result = percent_value * eval(after_percent)
                else:
                    result = percent_value
                clear_display(display)
                display.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("错误", "无效的百分比表达式")
        clear_display(display)

def calculate(display):
    try:
        expression = display.get()
        if '%' in expression:
            calculate_percentage(display)
            return
        
        expression = expression.replace('×', '*').replace('÷', '/')
        result = eval(expression)
        clear_display(display)
        display.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("错误", "无效的表达式")
        clear_display(display)

def insert_pi(display):
    display.insert(tk.END, str(math.pi))
