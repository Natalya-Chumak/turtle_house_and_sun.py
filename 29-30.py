import turtle
turtle.bgcolor("#6095f0")
turtle.shape("turtle")

for i in range(3):
    turtle.fd(300)
    turtle.right(90)
else:
    turtle.fd(300)
# turtle.fd(300)
# turtle.right(90)
# turtle.fd(300)
# turtle.right(90)


turtle.color("black", "#7926d1")
turtle.begin_fill()
turtle.right(45)
turtle.fd(212.5)
turtle.right(90)
turtle.fd(212.5)
turtle.end_fill()


turtle.penup()
turtle.right(45)
turtle.forward(300)
turtle.right(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)
turtle.fd(200)
turtle.right(90)
turtle.fd(100)
turtle.right(90)
turtle.fd(200)
turtle.penup()
turtle.right(90)
turtle.fd(20)
turtle.right(90)
turtle.fd(100)
turtle.pendown()

turtle.color("black", "#7926d1")
turtle.stamp()

# turtle.penup()
# turtle.left(90)
# turtle.fd(320)
# turtle.right(45)
# turtle.fd(150)



turtle.penup()
turtle.left(90)
turtle.fd(300)
turtle.right(90)
turtle.fd(300)


turtle.color("#edc13e")
turtle.speed(9)
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
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


# turtle.penup()
# turtle.right(180)
# turtle.fd(130)
# turtle.pendown()
# turtle.right(160)
# turtle.fd(130)
# turtle.penup()
# turtle.right(180)
# turtle.fd(130)
# turtle.pendown()
# turtle.right(160)
# turtle.fd(130)
# turtle.penup()
# turtle.right(180)
# turtle.fd(130)
# turtle.pendown()
# turtle.right(160)
# turtle.fd(130)
# turtle.penup()
# turtle.right(180)
# turtle.fd(130)
# turtle.pendown()
# turtle.right(160)
# turtle.fd(130)
# turtle.penup()
# turtle.right(180)
# turtle.fd(130)
# turtle.pendown()
# turtle.right(160)
# turtle.fd(130)
# turtle.penup()
# turtle.right(180)


turtle.mainloop() #не закрывает окно









# '''
# Сокращенные записи программного кода
# '''
#
# # import random
# a = -10
# b = 10
# from random import randint
# list1 = []
# for i in range (0, 10):
#     list1.append(randint(a,b))
#     print(list1[i], end='') #печать по 1 элементу
# print(f'\n{list1}') #печать всего списка
# list1 = [randint(-10,10) for _ in range(10)]
# print(f'\nlist1: {list1}') #печать всего списка
# list2 = [randint(-10,10) for _ in range(10)]
# print(f'\nlist2: {list2}') #печать всего списка
# list3 = list1 + list2
# print(f'\nlist3: {list3}') #печать всего списка
# list4 = list(set(list3))
# print(f'\nlist4: {list4}') #печать всего списка
# '''
#
# '''
# list5 = [i for i in list1 if i not in list2] + [i for i in list2 if i not in list1]
# print(f'list5:  {list(set(list5))}')