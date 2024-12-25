
import tkinter as tk

def clickbtn(value):
    current = enter.get()
    enter.delete(0, tk.END)
    enter.insert(0, current + value)

def clear():
    enter.delete(0, tk.END)

def calculate():
    try:
        result = eval(enter.get())
        enter.delete(0, tk.END)
        enter.insert(0, str(result))
    except Exception as e:
        enter.delete(0, tk.END)
        enter.insert(0, "Ошибка")

root = tk.Tk()

root.geometry("225x255")
root.title("Калькулятор")


enter_d = tk.StringVar()
enter = tk.Entry(root, width=20, font=40, textvariable=enter_d)
enter.place(x=20, y=10)


btn1 = tk.Button(root, width=5, height=2, text="1", command=lambda: clickbtn("1"))
btn2 = tk.Button(root, width=5, height=2, text="2", command=lambda: clickbtn("2"))
btn3 = tk.Button(root, width=5, height=2, text="3", command=lambda: clickbtn("3"))
btn4 = tk.Button(root, width=5, height=2, text="4", command=lambda: clickbtn("4"))
btn5 = tk.Button(root, width=5, height=2, text="5", command=lambda: clickbtn("5"))
btn6 = tk.Button(root, width=5, height=2, text="6", command=lambda: clickbtn("6"))
btn7 = tk.Button(root, width=5, height=2, text="7", command=lambda: clickbtn("7"))
btn8 = tk.Button(root, width=5, height=2, text="8", command=lambda: clickbtn("8"))
btn9 = tk.Button(root, width=5, height=2, text="9", command=lambda: clickbtn("9"))
btn0 = tk.Button(root, width=5, height=2, text="0", command=lambda: clickbtn("0"))
btnC = tk.Button(root, width=5, height=2, text="C", command=clear)
btnm = tk.Button(root, width=5, height=2, text="-", command=lambda: clickbtn("-"))
btnp = tk.Button(root, width=5, height=2, text="+", command=lambda: clickbtn("+"))
btnu = tk.Button(root, width=5, height=2, text="*", command=lambda: clickbtn("*"))
btnd = tk.Button(root, width=5, height=2, text="/", command=lambda: clickbtn("/"))
btnra = tk.Button(root, width=5, height=2, text="=", command=calculate)


btn1.place(x=15, y=50)
btn2.place(x=65, y=50)
btn3.place(x=115, y=50)
btn4.place(x=15, y=95)
btn5.place(x=65, y=95)
btn6.place(x=115, y=95)
btn7.place(x=15, y=140)
btn8.place(x=65, y=140)
btn9.place(x=115, y=140)
btn0.place(x=15, y=185)
btnC.place(x=65, y=185)
btnm.place(x=165, y=185)
btnp.place(x=165, y=140)
btnu.place(x=165, y=95)
btnd.place(x=165, y=50)
btnra.place(x=115, y=185)

root.mainloop()




