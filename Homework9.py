



def find_sum_elements(nums, target):
    # сначала проверим, есть ли в массиве отрицательные числа
    # если в массиве отсутствуют отрицательные числа, то нужно добавить в массив target,
    # отсортировать по возрастанию и получить срез до самого target, чтобы сократить массив для поиска
    num_index1 = 0
    num_index2 = 1
    nums.sort()
    if nums[0] >= 0:
        nums.append(target)
        nums.sort()
        nums = nums[:nums.index(target)]
    else:
        pass

    nums_check = []
    for num in nums:
        if (target-num) in nums_check:
            num_index1 = nums.index(num)
            num_index2 = nums_check.index(target-num)
            return [num_index1, num_index2]
        else:
            nums_check.append(num)
    return [num_index1, num_index2]


def test_task_1():
    tests = (
        ([2, 11, 15, 7], 9),
        ([3, 2, 4], 6),
        ([0, 0, 1], 0),
        ([3, 2, 1], 4),
        ([1, 3, 6, 7, 9], 10),
        ([-22, -24, 2, 11, 15, 7], 9)
    )
    num_correct = 0
    for nums, target in tests:
        result = find_sum_elements(nums, target)
        if not isinstance(result, list):
            print(f'find_sum_elements() должна возвращать массив, а не {type(result)} (nums={nums}, target={target})')
            continue
        if len(result) != 2:
            print(f'find_sum_elements() должна возвращать массив из двух элементов (nums={nums}, target={target})')
            continue
        if result[0] == result[1]:
            print(f'find_sum_elements() вернула два одинаковых индекса')
            continue
        if result[0] >= len(nums) or result[1] >= len(nums):
            print(f'Один из индексов выходит за границы nums')
            continue
        if nums[result[0]] + nums[result[1]] != target:
            print(f'Сумма элементов nums={nums} с индексами {result[0]} и {result[1]} не равна {target}')
            continue
        num_correct += 1
    print()
    print(f'Количество правильно решённых тестов: {num_correct} из {len(tests)}')
    if num_correct == len(tests):
        print('Отличный результат!')

test_task_1()

def is_pangram(text):

    text = list(set(text.lower()))
    text.sort()
    delimiters = [';', ',', ':', '.', '|', '!', '?', ' ']

    alfpabet = set(['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
                    'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
                    'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                    'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])
    for delimiter in delimiters:
        if delimiter in text:
            text.pop(text.index(delimiter))

    for c in text:
        if not (c >= 'а' and c <= 'ё'):
            return False
    text = set(text)
    if text == alfpabet:
        return True
    else:
        return False

def test_task_2():
    tests = (
        ('Съешь же ещё этих мягких французских булок да выпей чаю', True),
        ('Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства', True),
        ('В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!', False),
        ('А роза упала на лапу Азора', False),
        ('Мои папа и мама! Я живу хорошо. Просто замечательно. У меня есть свой дом', False),
    )
    num_correct = 0
    for test, correct_answer in tests:
        result = is_pangram(test)
        if result != correct_answer:
            print(f'Проверьте свою функцию на строке "{test}"')
            continue
        num_correct += 1
    print()
    print(f'Количество правильно решённых тестов: {num_correct} из {len(tests)}')
    if num_correct == len(tests):
        print('Отличный результат!')

test_task_2()