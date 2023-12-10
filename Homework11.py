# import requests
# from requests import HTTPError
#
#
# # На вход принимаем нужный http-код, по умолчанию - 200 (Нормальное завершение запроса)
# def send_request(status_code=200):
#     # Функция requests.get отправляет GET-запрос по указанному URL и возвращает ответ
#     response = requests.get("https://httpstat.us/%d" % status_code)
#
#     # По-умолчанию библиотека requests не выбрасывает исключения при кодах, означающих ошибку
#     # исключение нужно вызвать самому при помощи функции raise_for_status
#     response.raise_for_status()
#
#     # Возвращаем код ответа
#     return response.status_code
#
# def user_input():
#     code = int(input("Введите http код для проверки >"))
#     return code
#
# # Читаем ввод пользователя и преобразуем строку из input в int
# while True:
#
#     try:
#         code = user_input()
#         break
#     except ValueError:
#         print('Введен некоректный код. Код должен содержать только цифры')
#
#
#
# # Задаём response_code в None, чтобы к блоку finally он в любом случае был задан
# response_code = None
# try:
#     # Отправляем запрос и получаем ответ
#     response_code = send_request(code)
#
# # Обработаем HTTPError https://requests.readthedocs.io/en/latest/api/#requests.HTTPError
# except HTTPError as ex:
#     # Выводим текст ошибки
#     print("Произошла ошибка при отправке HTTP-запроса: %s" % str(ex))
#
#     # Меняем переменную response_code
#     response_code = ex.response.status_code
# finally:
#     print("Получен код:")
#     # Выводим на экран response_code
#     print(response_code)
#
# filename = 'product.txt'
#
#
# def read_user_file(filename):
#     with open(filename, mode='r', encoding='utf-8') as file:
#         lines_list = file.readlines()
#     return len(lines_list)
# file_name = 'product.txt'
# try:
#     quantity = read_user_file(filename=file_name)
#     print(quantity)
# except FileNotFoundError:
#     print('файл не найден')


def printing(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        print('result =', result)
        return result
    return inner

def add_one(x):
    return x + 1

add_one = printing(add_one)
y = add_one(10)



