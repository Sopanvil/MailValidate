import time
import requests


# Получаем данные
request = requests.get('some_adress')
request = request.json()

# Функция проверки
def mail_validate(r):
    #C параметром 'r' мы передавали бы параметры в функцию
    time.sleep(1)

# Предположим, что мы тянем данные по API
# Функция перебора, валидации и счетчика
def validator():
    counter_of_true = 0 # Счетчик
    for r in request:
        # Проверям, прошел ли адресс валидацию
        if mail_validate(r['some_email_id_in json']) == True:
            counter += 1

validator()