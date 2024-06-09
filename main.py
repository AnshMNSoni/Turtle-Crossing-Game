# Turtle Crossing Game:

from turtle import Screen
from TurtleClass import Object
from obstacles import Obstacles
import time

screen = Screen()
screen.setup(height=800, width=1000)


obj = Object()
cars = Obstacles()


screen.tracer(1)
screen.listen()
screen.onkey(fun=obj.up, key='Up')
screen.onkey(fun=obj.down, key='Down')
screen.update()

count = 1
game_is_on = True
while game_is_on:
    cars.create_cars()
    
    for go in range(count):  
            time.sleep(0.001)      
            screen.update()
            tle = cars.car_list[go]
            tle.back(25)
            
            dis = cars.car_list[go].distance(obj.pos())
            if (dis <= 30):
                screen.clearscreen()
                game_is_on = False
                obj.gameover()
            
            
            if (obj.ycor() >= 370):
                game_is_on = False
                screen.clearscreen()
                obj.win()
    
    screen.update()
    count += 1  

screen.exitonclick()