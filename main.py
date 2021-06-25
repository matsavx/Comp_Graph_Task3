import math
from tkinter import *


def exit_(event):
    root.destroy()


def draw_tree(x, y, side, fi, alfa, deep, count_deep):
    x1 = x
    y1 = y

    dx = side * math.sin(fi)
    dy = side * math.cos(fi)

    x2 = x + dx
    y2 = y - dy

    x3 = x + dx - dy
    y3 = y - dy - dx

    x4 = x - dy
    y4 = y - dx

    x5 = x - dy + side * math.cos(alfa) * math.sin(fi - alfa)
    y5 = y - dx - side * math.cos(alfa) * math.cos(fi - alfa)

    if count_deep < 5:
        colour = "#" + str(count_deep * 20) + "0000"
    elif count_deep < 9:
        colour = "#00" + str(count_deep * 10) + "00"
    else:
        colour = "#009900"

    canv.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=colour)
    canv.create_polygon(x4, y4, x3, y3, x5, y5, fill=colour)

    if deep > 1:
        draw_tree(x5, y5, side * math.sin(alfa), fi - alfa + math.pi / 2, alfa, deep - 1, count_deep + 1)
        draw_tree(x4, y4, side * math.cos(alfa), fi - alfa, alfa, deep - 1, count_deep + 1)


# инициализация окна
root = Tk();
root.title("Pifagor's tree")
root.bind('<Control-z>', exit_)
# создание холста
canv = Canvas(root, width=1800, height=1200, bg="lightblue")
canv.pack()

x = 600
y = 650
side = 100
deep = 15
alfa = math.pi / 3

canv.create_rectangle(0, 1200, 1800, 1200 - y, fill="#ADFF2F")

draw_tree(x / 2 - 100, y - 100, side / 2, math.pi / 2, alfa * 3 / 4, deep, 1)
draw_tree(x, y, side, math.pi / 2, alfa, deep, 1)

root.mainloop()
