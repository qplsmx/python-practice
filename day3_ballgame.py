# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

num = [[10,20,30],[40,50,60]]
print(num[0],[0])
print(num[0],[1])
print(num[0],[2])
print(num[1],[0])
print(num[1],[1])
print(num[1],[2])

num[1][2] = 100
print(num)


# %%

import turtle

pos_list = [ [100, 100],
            [100, -100],
            [-100, 100],
            [-100, -100] ]

for i in range(len(pos_list)):
    t = turtle.Turtle()
    t.shape("turtle")
    t.goto(pos_list[i][0],pos_list[i][1])
    
turtle.exitonclick()
turtle.bye()

# %%

import turtle

pos_list = [ [100, 100],
            [100, -100],
            [-100, 100],
            [-100, -100] ]

for pos_each in pos_list:
    t = turtle.Turtle()
    t.shape("turtle")
    t.goto(pos_each[0],pos_each[1])
    
turtle.exitonclick()
turtle.bye()

# %%

import turtle


pos_list = [ [100, 100],
            [100, -100],
            [-100, 100],
            [-100, -100] ]

t_list = []
for i in range(len(pos_list)):
    t = turtle.Turtle()
    t.shape("turtle")
    t_list.append(t)
    
for i in range(len(t_list)):
    t_list[i].goto(pos_list[i][0],pos_list[i][1])
    

turtle.exitonclick()
turtle.bye

# %%

import turtle       #기말과제에 쓸 속도 코드
t = turtle.Turtle()
t.shape("turtle")

x = 0
y = 0
x_vel = 0
y_vel = 3

for i in range(100):
    x = x + x_vel
    y = y + y_vel
    t.goto(x,y)

turtle.exitonclick()
turtle.bye()

# %%


import turtle


t = turtle.Turtle()
t.shape("turtle")

pos_list = [ [0, 0],
            [0, 0],
            [0, 0]]

vel_list = [ [-2,0],
            [0,2],
            [-2,2] ]

t_list = []

for i in range(len(pos_list)):
    t = turtle.Turtle()
    t.shape("turtle")
    t_list.append(t)
    
for i in range(100):
    for i in range(len(pos_list)):
        pos_list[i][0] = pos_list[i][0] + vel_list[i][0]
        pos_list[i][1] = pos_list[i][1] + vel_list[i][1]
        
        t_list[i].goto(pos_list[i][0], pos_list[i][1])
        
turtle.exitonclick()
turtle.bye()


# %%


import turtle

tline = turtle.Turtle()


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

tline.up()
tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
tline.down()

tline.goto(-SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
tline.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
tline.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

turtle.exitonclick()
turtle.bye()

# %%

import turtle

def outline():
    
    tline.up()
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.down()

    tline.goto(-SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 400

outline()
turtle.exitonclick()
turtle.bye()

# %%

import turtle

def outline():
    
    tline = turtle.Turtle()
    
    tline.up()
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.down()

    tline.goto(-SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

outline()

asteroid = turtle.Turtle()
asteroid.shape("circle")

loc = [0, 0]
vel = [5, 0]

asteroid.goto(loc[0], loc[1])

for i in range(150):
    loc[0] = loc[0] + vel[0]
    loc[1] = loc[1] + vel[1]
    
    asteroid.goto(loc[0], loc[1])
    
    if loc[0] >= SCREEN_WIDTH/2:
        vel[0] = -vel[0]
    
    if loc[0] <= SCREEN_WIDTH/-2:
        vel[0] = -vel[0] 
        
    
turtle.exitonclick()
turtle.bye()


# %%



import turtle

def outline():
    
    tline = turtle.Turtle()
    
    tline.up()
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.down()

    tline.goto(-SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

outline()

asteroid = turtle.Turtle()
asteroid.shape("circle")

loc = [0, 0]
vel = [0, 5]

asteroid.goto(loc[0], loc[1])

for i in range(150):
    loc[0] = loc[0] + vel[0]
    loc[1] = loc[1] + vel[1]
    
    asteroid.goto(loc[0], loc[1])
    
    if loc[0] >= SCREEN_WIDTH/2:
        vel[0] = -vel[0]
    
    if loc[0] <= SCREEN_WIDTH/-2:
        vel[0] = -vel[0] 

    if loc[1] >= SCREEN_HEIGHT/2:
        vel[1] = -vel[1]
    
    if loc[1] <= SCREEN_HEIGHT/-2:
        vel[1] = -vel[1]
        
    
turtle.exitonclick()
turtle.bye()
