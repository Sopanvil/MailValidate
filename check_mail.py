import threading
import time


def mail_validate():
    # В пол часа максимум 1800
    for i in range(10):
        time.sleep(1)


# Время начала выполнения
start = time.time()

t_l = []

# 1кк / 1800 ~= 556
for i in range(556):
    t = threading.Thread(target=mail_validate,
                         name='Thread-{}'.format(i+1))
    t_l.append(t)
    t.start()

for i in t_l:
    i.join()
    if i.is_alive() != False:
        print('{} - Что-то пошло не так'.format(i.name))

# Конец выполнения
end = time.time()

print('Время - ', end - start)
