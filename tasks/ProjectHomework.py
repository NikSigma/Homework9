import turtle


def start_game(x, y):
    global num_players


    while True:
        try:
            num_players = int(screen.textinput("Кількість гравців", "Введіть кількість гравців (1-5):"))
            if 1 <= num_players <= 5:
                break
            else:
                screen.textinput("Помилка", "Будь ласка, введіть число від 1 до 5.\n(Натисніть OK і спробуйте знову)")
        except:
            screen.textinput("Помилка", "Невірне введення. Введіть число від 1 до 5.\n(Натисніть OK і спробуйте знову)")

    print(f"Кількість гравців: {num_players}")
    

    pen.clear()
    pen.penup()
    pen.goto(-350, -250) 
    pen.pendown()
    pen.color("black")
    pen.pensize(3)
    for _ in range(2):
        pen.forward(700) 
        pen.left(90)
        pen.forward(500)  
        pen.left(90)

    start_x, start_y = -350, -200

    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.color("blue")
    pen.forward(700)

    finish_x, finish_y = -350, 200

    pen.penup()
    pen.goto(finish_x, finish_y)
    pen.pendown()
    pen.color("red")
    pen.forward(700)

    pen.penup()
    pen.goto(start_x - 40, start_y - 20)
    pen.color("blue")
    pen.write("Старт", font=("Arial", 16, "bold"))
    pen.goto(finish_x - 40, finish_y + 20)
    pen.color("red")
    pen.write("Фініш", font=("Arial", 16, "bold"))

    pen.hideturtle()

    
    turtles = []
    colors = ["red", "blue", "green", "yellow", "gray"]
    shapes = ["turtle", "circle", "square", "triangle", "arrow"]
    for i in range(num_players):
        t = turtle.Turtle()
        t.color(colors[i])
        t.shape(shapes[i])
        t.penup()
        t.goto(start_x + (700 / (num_players + 1)) * (i + 1), start_y)
        t.pendown()
        turtles.append(t)


screen = turtle.Screen()
pen = turtle.Turtle()


pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.color("blue")
pen.begin_fill()
for _ in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
pen.end_fill()


pen.penup()
pen.goto(0, -20)
pen.color("white")
pen.write("Почати гру", align="center", font=("Arial", 16, "bold"))
pen.hideturtle()


screen.onscreenclick(start_game, 1)


screen.mainloop()
