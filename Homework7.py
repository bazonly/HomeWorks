
from math import sqrt


def discriminant(a, b, c):
    """Функция для вычисления дискриминанта \n возвращать значение, посчитанное по формуле b**2 - 4 * a * c"""
    discr = b ** 2 - 4 * a * c
    return discr


def solve(a, b, c):
    """Функция, которая вычисляет корни квадратного уравнения"""
    # 1. Вычислить дискриминант с использованием функции discriminant и сохранить результат в переменную d
    d=discriminant(a=a,b=b,c=c)
    # 2. Если d < 0, печатать сообщение "Корней нет"
    # 3. Если d == 0, печатать сообщение "Один корень, x = <значение>"
    #    Формула, по которой считается корень в этом случае: x = - b / 2 / a
    # 4. Если d > 0, печатать сообщение "Два корня, x1 = <первое значение>, x2 = <второе значение>"
    #    Формулы, по которым считаются корни:
    #        x1 = (-b + sqrt(d)) / 2 / a
    #        x2 = (-b - sqrt(d)) / 2 / a

    # Для печати результатов рекомендуется использовать f-строки
    if d<0:
        print("Корней нет")
    elif d==0:
        x = -b/(2*a)
        print('Один корень, х = {}'.format(x))
    else:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b + sqrt(d))/(2*a)
        print('Два корня, x1 = {}, x2 = {}'.format(x1, x2))

solve(1, 2, 1)
solve(2, 5, 3)
solve(1, -1, 3)

def average_age_value(persons, gender):

    ages = []
    for person in persons:
        if person['gender'].lower() == gender:
            ages.append(int(person['age']))

    return sum(ages)/len(ages)

person1 = {'name': 'Alex',
           'age': 21,
           'gender': 'Male'}
person2 = {'name': 'Nika',
           'age': '35',
           'gender': 'Female'}
person3 = {'name': 'max',
           'age': '35',
           'gender': 'male'}
person4 = {'name': 'alexa',
           'age': '16',
           'gender': 'female'}
person5 = {'name': 'Maria',
           'age': '41',
           'gender': 'Female'}

persons = [person1, person2, person3, person4, person5]

average = average_age_value(persons, "female")
print(average)
