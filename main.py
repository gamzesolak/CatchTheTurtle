import random
import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ('Arial',30,'normal')
score = 0
game_over = False

#turtle list:
turtle_list = []
#Score turtle
score_turtle = turtle.Turtle()
#countdown turtle
countdown_turtle = turtle.Turtle()
#make turtle properties
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinares = [20, 10, 0, -10]
grid_size = 10

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score:0",move=False,align="center",font=FONT)

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score # yazarsak yukarıdaki skor değişkenini hatırlar
        score += 1 #skoru 1 arttır.
        score_turtle.clear() #üstüste yazmasın diye
        score_turtle.write(arg=f"Score:{score}", move=False, align="center", font=FONT)
        print(x,y)


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size ,y * grid_size)
    turtle_list.append(t)  #Herbir oluşturulan turtle ı bir dizide saklar

def setup_turtles():

    for x in x_coordinates:
        for y in y_coordinares:
            make_turtle(x,y)

def hide_turtles():  #turtle'ları gizle
    for t in turtle_list:
        t.hideturtle()

#recursive function = Bir fonksiyonun içinde kendisini çağırmak.
def show_turtles_randomly():
    if not game_over:
        hide_turtles() #bir önceki turtle sı gizle
        random.choice(turtle_list).showturtle()  #rastgele bir turtle göster
        screen.ontimer(show_turtles_randomly,500) #bu fonksiyonun içinde kendisini 500 milisaniyede bir çalıştır.

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setpos(0,y-30)
    countdown_turtle.clear()
    if time > 0 :
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time),move=False,align="center",font=FONT)
        screen.ontimer(lambda :countdown(time - 1),1000) # Saniyede bir bunu değiştir
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!".format(time), move=False, align="center", font=FONT)

def start_game_up():
    turtle.tracer(0)  #takip edici ilk sıfır yapılır
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)  #Bütün fonk çağırdıktan sonra 1 yap .Görevi Setup bölgesindeki animasyonları sıfırlamak.

start_game_up()
turtle.mainloop()
