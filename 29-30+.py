import turtle
import math
turtle.bgcolor("#6095f0")
turtle.shape("turtle")

a = 300 #длина стены дома
# основание дома
for i in range(3):
    turtle.fd(a)
    turtle.right(90)
else:
    turtle.fd(a)

# крыша c заливкой
turtle.color("black", "#7926d1")
turtle.begin_fill()
corner = 45
b = math.sqrt(a*a/2)
for i in range(1,2+1):
    turtle.right(corner*i)
    turtle.fd(b)
turtle.end_fill()

# путь к двери
turtle.penup()
turtle.right(45)
turtle.forward(300)
turtle.right(90)
turtle.fd(200)

# дверь
turtle.pendown()
turtle.right(90)
turtle.fd(200)
turtle.right(90)
turtle.fd(100)
turtle.right(90)
turtle.fd(200)

# путь к ручке
turtle.penup()
turtle.right(90)
turtle.fd(20)
turtle.right(90)
turtle.fd(100)

# ручка
turtle.pendown()
turtle.color("black", "#7926d1")
turtle.stamp()

# путь к солнцу
turtle.penup()
turtle.left(90)
turtle.fd(300)
turtle.right(90)
turtle.fd(300)

# солнце
turtle.color("#edc13e")
turtle.speed(11)
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

# лучи
turtle.pendown()
turtle.pensize(6)
turtle.right(90)
turtle.fd(50)
for i in range(17):
    turtle.penup()
    turtle.right(180)
    turtle.fd(130)
    turtle.pendown()
    turtle.right(160)
    turtle.fd(130)
else:
    turtle.penup()
    turtle.right(180)
    turtle.fd(130)

turtle.mainloop() #не закрывает окно
