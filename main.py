from tkinter import *


def btnclick(number):
    global val
    val = val + str(number)
    data.set(val)


def btnclear():
    global val
    val = ""
    data.set("")


def btnsamdeng():
    try:
        global val
        result = str(eval(val))
        data.set(result)

    except (ZeroDivisionError):
        val = ""
        data.set("Tidak Dapat Dibagi 0")

    except (SyntaxError, NameError):
        val = ""
        data.set("syntax error")



root = Tk()
root.resizable(0, 0)
root.title("Kalkulator")
root.geometry("360x380")
val = " "
data = StringVar()  # convert button click to string variable

# main display
display = Entry(root, bd = 29, textvariable = data, justify = "right", bg = "grey", font = ("ariel", 20))
display.grid(row = 0, columnspan = 4)

# button
btn1 = Button(root, text = "1", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(1))
btn2 = Button(root, text = "2", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(2))
btn3 = Button(root, text = "3", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(3))
btn4 = Button(root, text = "4", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(4))
btn5 = Button(root, text = "5", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(5))
btn6 = Button(root, text = "6", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(6))
btn7 = Button(root, text = "7", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(7))
btn8 = Button(root, text = "8", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(8))
btn9 = Button(root, text = "9", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(9))
btn0 = Button(root, text = "0", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
              command = lambda: btnclick(0))

btnplus = Button(root, text = "+", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
                 command = lambda: btnclick('+'))
btnmin = Button(root, text = "-", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
                command = lambda: btnclick('-'))
btnkali = Button(root, text = "*", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
                 command = lambda: btnclick('*'))
btnbagi = Button(root, text = "/", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
                 command = lambda: btnclick('/'))
btnsamdeng = Button(root, text = "=", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
                    command = btnsamdeng)
btnclear = Button(root, text = "C", font = ("ariel", 12, "bold"), bd = 12, height = 2, width = 6,
                  command = btnclear)

# positioning
btn1.grid(row = 3, column = 0)
btn2.grid(row = 3, column = 1)
btn3.grid(row = 3, column = 2)
btn4.grid(row = 2, column = 0)
btn5.grid(row = 2, column = 1)
btn6.grid(row = 2, column = 2)
btn7.grid(row = 1, column = 0)
btn8.grid(row = 1, column = 1)
btn9.grid(row = 1, column = 2)
btn0.grid(row = 4, column = 1)

btnplus.grid(row = 1, column = 3)
btnmin.grid(row = 2, column = 3)
btnkali.grid(row = 3, column = 3)
btnbagi.grid(row = 4, column = 2)
btnsamdeng.grid(row = 4, column = 3)
btnclear.grid(row = 4, column = 0)

root.mainloop()
