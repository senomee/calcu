from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    nilai.set(expression)


def samadengan():
    try:
        global expression
        total = str(eval(expression))
        nilai.set(total)
        expression = ""
    except:
        nilai.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    nilai.set("")


if __name__ == "__main__":
    ui = Tk()
    ui.resizable(0,0) #biar ga bisa di resize
    ui.configure(background = "white")
    ui.title("Kalkulator")
    ui.geometry("235x370") #ukuran
    nilai = StringVar()
    ui = Tk()
    ui.resizable(0, 0) #biara gabisa di resize
    ui.configure(background = "white")
    ui.title("Kalkulator")
    ui.geometry("235x370")
    menu = Entry(ui, textvariable = nilai)

    menu.grid(columnspan = 4, ipadx = 10.)
    # fungsi
    b0 = Button(ui, text = ' 0 ', fg = 'white', bg = 'grey', command = lambda: press(0), height = 4, width = 7)
    b00 = Button(ui, text = ' 00 ', fg = 'white', bg = 'grey', command = lambda: press(00), height = 4, width = 7)
    b1 = Button(ui, text = ' 1 ', fg = 'white', bg = 'grey', command = lambda: press(1), height = 4, width = 7)
    b2 = Button(ui, text = ' 2 ', fg = 'white', bg = 'grey', command = lambda: press(2), height = 4, width = 7)
    b3 = Button(ui, text = ' 3 ', fg = 'white', bg = 'grey', command = lambda: press(3), height = 4, width = 7)
    b4 = Button(ui, text = ' 4 ', fg = 'white', bg = 'grey', command = lambda: press(4), height = 4, width = 7)
    b5 = Button(ui, text = ' 5 ', fg = 'white', bg = 'grey', command = lambda: press(5), height = 4, width = 7)
    b6 = Button(ui, text = ' 6 ', fg = 'white', bg = 'grey', command = lambda: press(6), height = 4, width = 7)
    b7 = Button(ui, text = ' 7 ', fg = 'white', bg = 'grey', command = lambda: press(7), height = 4, width = 7)
    b8 = Button(ui, text = ' 8 ', fg = 'white', bg = 'grey', command = lambda: press(8), height = 4, width = 7)
    b9 = Button(ui, text = ' 9 ', fg = 'white', bg = 'grey', command = lambda: press(9), height = 4, width = 7)

    koma = Button(ui, text = '.', fg = 'white', bg = 'grey', command = lambda: press('.'), height = 4, width = 7)
    tambah = Button(ui, text = ' + ', fg = 'white', bg = 'grey', command = lambda: press("+"), height = 4, width = 7)
    kurang = Button(ui, text = ' - ', fg = 'white', bg = 'grey', command = lambda: press("-"), height = 4, width = 7)
    kali = Button(ui, text = ' * ', fg = 'white', bg = 'grey', command = lambda: press("*"), height = 4, width = 7)
    bagi = Button(ui, text = ' / ', fg = 'white', bg = 'grey', command = lambda: press("/"), height = 4, width = 7)
    clear = Button(ui, text = 'Clear', fg = 'white', bg = 'grey', command = clear, height = 4, width = 16)
    samdeng = Button(ui, text = ' = ', fg = 'white', bg = 'grey', command = samadengan, height = 4, width = 16)

    # layout
    # 0 -[    Jawaban     ]
    # 1 -[7]  [8]  [9]  [+]
    # 2 -[4]  [5]  [6]  [-]
    # 3 -[1]  [2]  [3]  [*]
    # 4 -[.]  [0]  [00] [/]
    # 5 -[ clear ] [  ==  ]
    #    (0)  (1)  (2)  (3)

    # penataan
    b0.grid(row = 5, column = 1)
    b00.grid(row = 5, column = 2)
    b1.grid(row = 4, column = 0)
    b2.grid(row = 4, column = 1)
    b3.grid(row = 4, column = 2)
    b4.grid(row = 3, column = 0)
    b5.grid(row = 3, column = 1)
    b6.grid(row = 3, column = 2)
    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

    koma.grid(row = 5, column = 0)
    tambah.grid(row = 2, column = 3)
    kurang.grid(row = 3, column = 3)
    kali.grid(row = 4, column = 3)
    bagi.grid(row = 5, column = 3)
    clear.place(x = 0, y = 303)
    samdeng.place(x = 118, y = 303)

    ui.mainloop()