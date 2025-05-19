# -*- coding: utf-8 -*-
score = 90
if score == 90:
    print("만점입니다")
print("수고하셨습니다")

# %%
num = int(input("양의정수:"))
if num%2 == 0:
    print("양수입니다")
else:
    print("홀수입니다")

# %%

num = int(input("나이를 입력하십시오:"))
if num < 20:
    print(">>>입장료:5000원")
else:
    print(">>>입장료:10000원")

# %%

num = int(input("양의 정수 입력:"))
if num > 0:
    print(">>>양수입니다")
if num == 0:
    print("양수도 음수도 아닙니다")
if num < 0:
    print(">>>음수입니다")
    
# %%

age = 15
height = 100
if(age >= 10):
    if(height >= 110):
        print(">>>탑승가능합니다")
    else:
        print(">>>키제한으로 탑승이 불가능합니다.")
        print("죄송합니다.")
else:
    print("나이제한으로 탑승이 불가능합니다.")
    print("죄송합니다.")

# %%

num = int(input("양의 정수를 입력하세요:"))
print()
print("양의 정수:"+str(num))
if num%2 == 0:
    if num%4 == 0:
        print("나머지가 0입니다")
    else:
        print("나머지가 2입니다")
else:
    if num%4 == 1:
        print("나머지가 1입니다")
    else:
        print("나머지가 3입니다")
        
# %%

age = 15
height = 180
if( age >= 10 and height >= 110):
    print(">>>탑승가능합니다")
else:
    print(">>>탑승불가능합니다")
    print(">>>죄송합니다.")
    
# %%














# %%

age = int(input("나이를 입력해주세요:"))
money = int(input("돈을 입력해주세요:"))
print()
print("나이:"+str(age))
print()
print("돈:"+str(money))
if age < 20:
    if money < 5000:
        print(">>>입장불가")
        print(">>>추가필요금액:"+str(5000-money))
    else:
        print(">>>입장가능")
        print(">>>거스름돈:"+str(money-5000))
             
else:
    if money < 10000:
        print(">>>입장불가")
        print(">>>추가필요금액:"+str(10000-money))
    else:
        print(">>>입장가능")
        print(">>>거스름돈:"+str(money-10000))
        
# %%

year = int(input("연도를 입력해주세요:"))
print()
print("year:"+str(year))
print()
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(str(year)+"년은 윤년입니다")
        else:
            print(str(year)+"년은 평년입니다")
    else:
        print(str(year)+"년은 윤년입니다")
        
else:
    print(str(year)+"년은 평년입니다")
