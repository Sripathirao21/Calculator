import tkinter as tk

calculate = " "

def add_to_calculate(symbol):
    global calculate
    calculate += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculate)

def evaluate_calculate():
    global calculate
    try:
        calculate = str(eval(calculate))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculate)
    except:
        clear_text()
        text_result.insert(1.0, "Error")
        pass

def clear_text():
    global calculate
    calculate = ""
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculate)

root = tk.Tk()
root.geometry("300x400")  
root.configure(bg="#f0f0f0") 


text_result = tk.Text(root, height=3, width=22, font=("Arial", 21), bg="#d9d9d9", fg="black")  
text_result.grid(row=0, column=0, columnspan=4)


btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculate(1), width=5, font=("Arial", 21), bg="#ffcccc", fg="black")
btn_1.grid(row=2, column=0)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculate(2), width=5, font=("Arial", 21), bg="#ffb3b3", fg="black")
btn_2.grid(row=2, column=1)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculate(3), width=5, font=("Arial", 21), bg="#ff9999", fg="black")
btn_3.grid(row=2, column=2)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculate(4), width=5, font=("Arial", 21), bg="#ffcccc", fg="black")
btn_4.grid(row=3, column=0)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculate(5), width=5, font=("Arial", 21), bg="#ffb3b3", fg="black")
btn_5.grid(row=3, column=1)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculate(6), width=5, font=("Arial", 21), bg="#ff9999", fg="black")
btn_6.grid(row=3, column=2)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculate(7), width=5, font=("Arial", 21), bg="#ffcccc", fg="black")
btn_7.grid(row=4, column=0)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculate(8), width=5, font=("Arial", 21), bg="#ffb3b3", fg="black")
btn_8.grid(row=4, column=1)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculate(9), width=5, font=("Arial", 21), bg="#ff9999", fg="black")
btn_9.grid(row=4, column=2)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculate(0), width=5, font=("Arial", 21), bg="#ffe6e6", fg="black")
btn_0.grid(row=5, column=1)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculate("+"), width=5, font=("Arial", 21), bg="#cce6ff", fg="black")
btn_plus.grid(row=2, column=3)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculate("-"), width=5, font=("Arial", 21), bg="#99ccff", fg="black")
btn_minus.grid(row=3, column=3)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculate("*"), width=5, font=("Arial", 21), bg="#66b3ff", fg="black")
btn_mul.grid(row=4, column=3)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculate("/"), width=5, font=("Arial", 21), bg="#3399ff", fg="black")
btn_div.grid(row=5, column=3)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculate("("), width=5, font=("Arial", 21), bg="#d9d9d9", fg="black")
btn_open.grid(row=5, column=0)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculate(")"), width=5, font=("Arial", 21), bg="#d9d9d9", fg="black")
btn_close.grid(row=5, column=2)

btn_clear = tk.Button(root, text="C", command=clear_text, width=11, font=("Arial", 14), bg="#ff6666", fg="white")  # Clear button
btn_clear.grid(row=6, column=0, columnspan=2)

btn_equals = tk.Button(root, text="=", command=evaluate_calculate, width=11, font=("Arial", 14), bg="#66ff66", fg="black")  # Equals button
btn_equals.grid(row=6, column=2, columnspan=2)

root.mainloop()
