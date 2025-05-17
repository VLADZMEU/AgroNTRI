import turtle
try:
    l = int(input("Число от -400 до 400: "))

except ValueError:
    print("Это не число")
    exit()

if l < -400 or l > 400:
    print("Число не входит в диапазон")
    exit()

t = turtle.Turtle()
t.shape('turtle')
t.forward(l)
turtle.done()
