import threading
import time
import requests
import multiprocessing


def mail_validate():
    # Заглушка со слипом
    time.sleep(1)

#Время начала выполнения
start = time.time()

for i in range(1000000):

    t = threading.Thread(target=mail_validate,
                         name='Thread{}'.format(i+1))
    t.start()

# Конец выполнения
end = time.time()

print('Время - ', end - start)
