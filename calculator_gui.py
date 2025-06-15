# calculator_gui.py
import tkinter as tk
from calculator_operations import *
from calculator_constants import BUTTON_LAYOUT

def create_calculator():
    root = tk.Tk()
    root.title("计算器")
    root.resizable(False, False)
    
    try:
        root.iconbitmap('Calculator.ico')
    except:
        pass  # 如果图标文件不存在则忽略
        
    # 创建菜单栏
    menubar = tk.Menu(root)
    
    # 创建"帮助"菜单
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="关于", command=show_about)
    menubar.add_cascade(label="帮助", menu=help_menu)
    
    root.config(menu=menubar)
    
    display = tk.Entry(root, font=('Arial', 20), justify='right', bd=10)
    display.grid(row=0, column=0, columnspan=5, sticky='nsew')

    # 创建按钮
    for (text, row, col) in BUTTON_LAYOUT:
        if text == '=':
            btn = tk.Button(root, text=text, command=lambda d=display: calculate(d),
                          font=('Arial', 14), bg='orange')
        elif text == 'C':
            btn = tk.Button(root, text=text, command=lambda d=display: clear_display(d),
                          font=('Arial', 14), bg='lightgray')
        elif text == '√':
            btn = tk.Button(root, text=text, command=lambda d=display: calculate_square_root(d),
                          font=('Arial', 14), bg='lightgreen')
        elif text == '⌫':
            btn = tk.Button(root, text=text, command=lambda d=display: delete_last_char(d),
                          font=('Arial', 14), bg='lightgray')
        elif text == '+/-':
            btn = tk.Button(root, text=text, command=lambda d=display: toggle_sign(d),
                          font=('Arial', 14), bg='lightblue')
        elif text == '^2':
            btn = tk.Button(root, text=text, command=lambda d=display: append_to_display(d, '**2'),
                          font=('Arial', 14), bg='lightblue')
        elif text == '^3':
            btn = tk.Button(root, text=text, command=lambda d=display: append_to_display(d, '**3'),
                          font=('Arial', 14), bg='lightblue')
        elif text == 'π':
            btn = tk.Button(root, text=text, command=lambda d=display: insert_pi(d),
                          font=('Arial', 14), bg='lightblue')
        elif text in '÷×+-()%':
            btn = tk.Button(root, text=text, command=lambda t=text, d=display: append_to_display(d, t),
                          font=('Arial', 14), bg='lightblue')
        else:
            btn = tk.Button(root, text=text, command=lambda t=text, d=display: append_to_display(d, t),
                          font=('Arial', 14))
            
        btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
        
    # 配置网格布局
    for i in range(7):
        root.grid_rowconfigure(i, weight=1)
    for j in range(5):
        root.grid_columnconfigure(j, weight=1)

    return root
    
def show_about():
    """显示关于对话框"""
    about_text = """计算器   
版本: 0.9.2"""
    messagebox.showinfo("关于", about_text)
