import threading
import time


def mail_validate():
    # В пол часа максимум 1800
    for i in range(1800):
        time.sleep(1)

#Время начала выполнения
start = time.time()

t_l = []

#1кк / 1800 ~= 556
for i in range(556):

    t = threading.Thread(target=mail_validate,
                         name='Thread{}'.format(i+1))
    t_l.append(t)
    t.start()

for i in t_l:
    i.join()

# Конец выполнения
end = time.time()

print('Время - ', end - start)
