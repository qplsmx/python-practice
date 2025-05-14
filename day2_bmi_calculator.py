# -*- coding: utf-8 -*-
"""
Created on Wed May 14 16:30:54 2025

@author: qplsm
"""

import turtle

def bmi(weight, height):
    height = height / 100      # cm => m
    result = weight / (height * height)
    return result

while True:
    weight = float(turtle.textinput("BMI", "몸무게"))
    if weight == 0:  # 무게가 0이면 종료
        break

    height = float(turtle.textinput("BMI", "키"))

    bmi_value = bmi(weight, height)
    print(bmi_value)

turtle.bye()


# %% 

# 환전계산기

import turtle

def change(mon, cont):
    if cont == "미국":
        TBR = 1117.5
    elif cont == "일본":
        TBR = 1022.56
    elif cont == "중국":
        TBR = 182.64
    elif cont == "영국":
        TBR = 1343.24
    else:
        print("잘못된 국가가 입력입니다.")
        return 0

    result = mon / TBR
    return result

while True:
    money = float(turtle.textinput("환전계산기", "KRW"))
    contry = turtle.textinput("환전계산기", "국가")

    if money == 0:
        break

    change_value = change(money, contry)
    print(change_value)

turtle.bye()