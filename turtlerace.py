from turtle import Turtle, Screen 
import random
is_race_on= False
y_val=-100
screen=Screen() 
screen.setup(width=1400, height=600)  
user_input= screen.textinput(title="Make your bet", prompt="which color turtle will win the race?")
colors=["red", "orange", "yellow", "green", "blue", "purple"] 
all_turtles=[] 
drawing_turtle=Turtle() 
drawing_turtle.speed(6)
drawing_turtle.hideturtle()  
drawing_turtle.penup()
drawing_turtle.goto(x=-410, y=-120) 
drawing_turtle.left(90) 
drawing_turtle.pendown()
drawing_turtle.forward(230) 
drawing_turtle.penup()
drawing_turtle.goto(x=450,y=120) 
drawing_turtle.right(180) 
drawing_turtle.pendown() 
drawing_turtle.forward(230)  
for turtle_index in range(0, 6): 
    new_turtle= Turtle(shape="turtle") 
    new_turtle.penup()  
    new_turtle.goto(x=-430, y=y_val)
    y_val+=35
    new_turtle.color(colors[turtle_index]) 
    all_turtles.append(new_turtle)

if user_input: 
    is_race_on=True 

while is_race_on: 
   
   for turtle in all_turtles: 
       if turtle.xcor()>430: 
           is_race_on=False 
           winning_color=turtle.pencolor() 
           if user_input== winning_color: 
                print(f"You won! The winning color is {winning_color}.") 
           else: 
                print(f"You lost! The winning color is {winning_color}.")
       
       moving_distance= random.randint(0,10)    
       turtle.forward(moving_distance)
       

screen.exitonclick()