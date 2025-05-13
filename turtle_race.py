
# %%

import turtle 
import random

t1_distance = 0
t2_distance = 0

t1 = turtle.Turtle()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.shape("turtle")

t1.color("blue")
t1.up()
t1.goto(0,200)
t1.down()

t2.color("red")
t2.up()
t2.goto(0,-200)
t2.down()

line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(300, 300)
line.pendown()
line.right(90)
line.forward(600)

result = turtle.Turtle()
result.hideturtle()
result.penup()
result.goto(0, 0)

while True:
    forecast = turtle.textinput("경주게임","파랑or빨강")
    if forecast == "파랑" or forecast == "빨강":
        break

while t1_distance <= 300 and t2_distance <= 300:
    t1_move = random.randint(1,10)
    t1.forward(t1_move)
    t1_distance += t1_move
    t2_move = random.randint(1,10)
    t2.forward(t2_move)
    t2_distance += t2_move
    print("t1:",t1_distance,"vs","t2:",t2_distance)
    
    
    if t1_distance >= 300 or t2_distance >= 300:
        if t1_distance > t2_distance:
            print("끝")
            output = "파랑"
            t1.write("승리", font=("Arial", 40))
            break
        elif t1_distance < t2_distance:
            print("끝")
            output = "빨강"
            t2.write("승리", font=("Arial", 40))
            break
        else:
            print("끝")
            output = "파랑"
            t1.write("승리", font=("Arial", 40))

if forecast == output:
    result.write("예측성공")
else:
    result.write("예측실패")
    
turtle.exitonclick()
    
        


