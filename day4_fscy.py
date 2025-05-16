# -*- coding: utf-8 -*-

# 연 나이 구하기 : 연나이 = 현재년도 - 출생년도

thisyear = 2025

birthyear = int(input("출생년도를 입력해주세요:"))

age = thisyear - birthyear

print("당신의 나이는 "+str(age)+"세 입니다.")

# %%
print("First Come First Serve Scheduling")

#process = [pid, arrival_time, brust_time]

process=[
    ['P1', 0, 10],
    ['P2', 1, 28],
    ['P3', 2, 6],
    ['P4', 3, 4],
    ['P5', 4, 14],
]

n = len(process)
gantt = [[],[],[]]
prirun = 0
run = 0

for a in range(0,n) :
    gantt[0].append(process[a][0])
    run = run + prirun
    arrive = process[a][1]
    wt = run - arrive 
    gantt[1].append(wt)
    tt = wt + process[a][2]
    gantt[2].append(tt)
    prirun = process[a][2]

print("간트차트:", gantt)

sum_wt = 0
sum_tt = 0

for i in range(0, n) :
    print(gantt[0][i], "대기시간 :", gantt[1][i] ,"\t", "반환시간 : ", gantt[2][i])
    sum_wt = sum_wt + gantt[1][i]
    sum_tt = sum_tt + gantt[2][i]
    
print("평균대기시간:", sum_wt/n, "\t", "평균반환시간:", sum_tt/n)