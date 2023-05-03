import math


# Задание 1
def task_1(x=3):

    if type(x) == str:
        return ('Ввдено не число')
    else:
        perimeter = x * 4  # периметр квадрата
        square = pow(x, 2)  # площадь квадрата
        diagonal = math.sqrt(2) * x  # диагональ квадрата

    return perimeter, square, diagonal


# Задание 2
def task_2(a=2, b=4, c=1):

    discriminant = pow(b, 2) - 4*a*c  # дискриминант

    if discriminant <= 0:  # проверка дискриминанта на корректность для задания
        return ('Дискриминант меньше или равен нулю, введите другие значения')
    else:
        x_1 = (-b + math.sqrt(discriminant))/(2*a)
        x_2 = (-b - math.sqrt(discriminant))/(2*a)

    return round(x_1, 2), round(x_2, 2)


# Задание 3
def task_3(line_1='Привет', line_2='Мир'):

    if len(line_1) <= 1:  # проверка на длину строки 1, подходящей для данного задания
        return ('Строка 1 слишком короткая')
    elif len(line_2) <= 1:  # проверка на длину строки 2, подходящей для данного задания
        return ('Строка 2 слишком короткая')
    else:
        modified_line_1 = line_2[:2] + line_1[2:]  # смена первых 2х символов в первой строке
        modified_line_2 = line_1[:2] + line_2[2:]  # смена первых 2х символов в0 второй строке
        end_line = modified_line_1 + ' ' + modified_line_2  # итоговая строка

    return end_line


# Задание 4
def task_4(line_1=r'D:\autotest_qa\honework_2.py'):

    dot_search = line_1.rfind('.')  # поиск индекса последней точки(стоит перед расширением конечного файла)
    last_slash = line_1.rfind('\\') + 1  # поиск индекса последнего "\"

    if dot_search == -1:
        return ("Точка не найдена, в строке нет файла")
    elif last_slash == 0:
        return ("Слэш не найден, в строке нет файла")
    else:
        name_file = line_1[last_slash: dot_search]
        disk_name = line_1[:1]
        root_folder_name = line_1[3:line_1.find('\\', 3)]

    total_info = '''
    Название диска - {}
    Название корневой папки - {}
    Имя файла - {}
    '''.format(disk_name, root_folder_name, name_file)

    return total_info


# Задание 5
def task_5(a=5, b=4):

    result = '''
    {} + {} = {}
    {} * {} = {}
    '''.format(a, b, a + b, a, b, a * b)

    return result


# Задание 6
def task_6(line_1='2121212121212121'):

    if type(line_1) == str:
        line_1 = line_1[::2]
    else:
        return ('Ввдена не строка')
    return line_1


# Задание 7
def task_7(line_1=r'wtf', line_2=r'brick quz jmpy veldt whangs fox'):

    # получение списка индексов символов первой строки
    line_1_ind = line_2.find(line_1[0]), line_2.find(line_1[1]), line_2.find(line_1[2])

    # получение новой искомой строки
    line_2 = line_2[min(line_1_ind): max(line_1_ind) + 1]

    return line_2


# print(task_1())
# print(task_2())
# print(task_3())
print(task_4())
# print(task_5())
# print(task_6())
# print(task_7())
