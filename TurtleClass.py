from turtle import Turtle, Screen

ALIGNMENT = 'Center'
FONT = ('Courier', 22, 'normal')

screen = Screen()

class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(1.3)
        self.speed('fastest')
        self.penup()
        self.goto(0, -370)
        self.setheading(90)
        
    def up(self):
        self.fd(20) 
        
    def down(self):
        self.bk(20)
    
    def win(self):
        t = Turtle()
        t.hideturtle()
        t.color('black')
        t.write(f':: Win ::', align=ALIGNMENT, font=FONT)

    def gameover(self):
        t = Turtle()
        t.hideturtle()
        t.color('black')
        t.write(f':: Game Over ::', align=ALIGNMENT, font=FONT)
    
        