import turtle
try:
    l = int(input("Введите число от -400 до 400: "))
except ValueError:
    print("Это не то число")
    exit()

if l < -400 or l > 400:
    print("Число не входит в диапазон")
    exit()

t = turtle.Turtle()
t.shape('turtle')

for i in range(4):
    t.forward(l)
    t.left(90)
turtle.done()
