import turtle
try:
    alfa = int(input("Введите число углов: "))
    l = int(input("Введите число от -100 до 100: "))
except ValueError:
    print("Это не то число")
    exit()

if l < -100 or l > 100:
    print("Число не входит в диапазон")
    exit()

t = turtle.Turtle()
t.shape('turtle')
t.teleport(-l, -l)
for i in range(alfa):
    t.forward(l)
    t.left(360/alfa)
turtle.done()