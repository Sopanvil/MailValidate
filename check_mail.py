import threading
import time
import requests
import multiprocessing


def mail_validate():
    # В пол часа максимум 1800
    for i in range(1800):
        time.sleep(1)

#Начало выполнения
start = time.time()

thread_list = []

#1кк / 1800 ~= 556
for i in range(556):

    t = threading.Thread(target=mail_validate,
                         name='Thread{}'.format(i+1))
    thread_list.append(t)
    t.start()

for i in thread_list:
    i.join()

# Конец выполнения
end = time.time()

print('Время - ', end - start)