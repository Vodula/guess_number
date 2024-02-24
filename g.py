from tkinter import *
import random
from tkinter import messagebox

root = Tk()
clicks = 0
max_clicks = 5
root.geometry("400x400")
root.title(f"Спроба {clicks}")


def gen_num():
    global c
    global clicks
    a = int(ent1.get())
    b = int(ent2.get())
    c = random.randint(a, b)
    messagebox.showinfo("Повідомлення", "Число згенеровано!")
    clicks = 0
    root.title(f"Спроба {clicks}")
    ent3.config(state="normal")


def guess():
    global c
    global clicks
    clicks += 1
    root.title(f"Спроба {clicks}")
    if clicks >= max_clicks:
        ent3.config(state="disabled")
        messagebox.showinfo("Повідомлення", "Вичерпано кількість спроб!")
    else:
        g = int(ent3.get())
        if g > c:
            messagebox.showinfo("Результат", "Загадане число менше")
        elif g < c:
            messagebox.showinfo("Результат", "Загадане число більше")
        else:
            messagebox.showinfo("Результат", f"Ви вгадали число {c}")
            ent3.config(state="disabled")
            cnt=messagebox.askokcancel('Вгадай число','Ви хочете продовжити гру?')
            if cnt==True:
                ent1.delete(0,END)
                ent2.delete(0, END)
                ent3.delete(0, END)
                gen_num()
            else:
                root.quit()

ent1 = Entry(root)
ent1.pack()
ent2 = Entry(root)
ent2.pack()
btn_gen = Button(root, text="Генерувати", command=gen_num)
btn_gen.pack()
ent3 = Entry(root)
ent3.pack()
btn_guess = Button(root, text="Вгадати", command=guess)
btn_guess.pack()

root.mainloop()
