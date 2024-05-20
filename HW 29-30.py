import math
from turtle import *
import random
from random import randint

bgcolor("#6095f0")
shape("turtle")
a = 50
b = 10
x = 0
y = 0
radius = 40


def draw_gift(x, y, a):
    # нижний прямоугольник
    penup()
    goto(x, y)
    pendown()
    for i in range(4):
        lt(-90)
        fd(a)
    penup()

    # верхний прямоугольник
    pendown()
    for i in range(4):
        if i==0:
            fd(b)
            lt(90)
        elif i==1 or i==3:
            fd(b*2)
            lt(90)
        elif i == 2:
            fd(a+b*2)
            lt(90)
    else:
       fd((a+b*2)/2)

    #ленточка
    penup()
    lt(-90)
    fd(a)
    lt(90*2)
    pendown()
    fd(a+b)
    penup()



    # бантик
f1 = 28
g1 = 72
f2 = 6
g2 = 32


def draw_petal(x, y):
    pendown()
    fd(10)
    for i in range (11+1):
        if i == 0 or i==5 or i==6 or i==11:
            r1 = f1  # радус окружности (полукруг)
            ext1 = g1 # угол сектора окружности
            circle(r1, ext1)
        else:
            r2 = f2  # радус окружности (полукруг)
            ext2 = g2  # угол сектора окружности
            circle(r2, ext2)

    penup()
    fd(100)

w = random.randint(0, 100)
z = random.randint(0, 100)
def draw_snowball(w,z):
    for i in range(8):
        if i%2==0:
            pendown()
            circle(8)
            penup()
            fd(100)
            lt(30)
        elif i% 3 == 0:
            pendown()
            circle(9)
            penup()
            fd(-210)
            lt(-190)
        else:
            pendown()
            circle(7)
            penup()
            fd(-180)
            lt(-44)

draw_gift(x, y, a)
draw_petal(x, y)
draw_snowball(w, z)

mainloop() #не закрывает окно

