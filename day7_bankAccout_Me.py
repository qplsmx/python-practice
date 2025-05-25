# -*- coding: utf-8 -*-
"""
Created on Sun May 25 13:16:16 2025

@author: qplsm
"""

import = threading.Lock()
balance = 0

def deposit():
    global balance
    lock.acquire()
    local_var = balance
    local_var += 1
    time.sleep(0.001)
    balance = local_var
    lock.release()
    
def withdraw():
    global balance
    lock.acquire()
    local_var = balance
    local_var -= 1
    time.sleep(0.001)
    balance = local_var
    lock.release()

for i in range(1000):
    t1 = threading.Thread(target=deposit)
    t2 = threading.Thread(target=withdraw)
    t1.start()
    t2.start()
    
t1.join()
t2.join()
print("잔액: ", balance)

# %%

import threading, time

semaphore = threading.Semaphore(2)

def access_resource(id):
    print(f"스레드{id} 세마포어 획득 waiting")
    semaphore.acquire()
    print(f"스레드{id} 세마포어 획득")
    tiem.sleep(2)
    semaphore.release()
    print(f"스레드{id} 세마포어 반납")
    
threads = []
for i in range(5):
    t = threading.Thread(target=access_resoource, args=(i,))
    thread.append(t)
    t.start()
    
for thread in threads:
    thread.join()
    
print("All threads End")

# %%

import threading, time

semaphore = threading.Semaphore(0)

def task1():
    print("task1 세마포어 획득 기다림")
    semaphore.acquire()
    print("task1 임계구역 진입")
    time.sleep(2)
    semaphore.release()
    print("task1 세마포어 반납")
    
th1 = threading.Thread(target=task1)
th1.start()
th2 = threading.Thread(targey=task2)
th2.start()
th1.join()
th2.join()
print("All thread End")

