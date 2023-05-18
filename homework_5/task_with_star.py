# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    """
    преобразование числа с арабскими цифрами в число с римскими числами

    :param val: рарабское число
    :return: roman_str - римское число
    """
    # словари с римской записью единиц, десятков и сотен
    units = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    dozens = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    hundreds = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}

    roman_str = 'M' * int(val // 1000) + hundreds[int(val % 1000)//100] + dozens[int((val % 1000) % 100) // 10] \
                + units[int(((val % 1000) % 100) % 10)]


    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


# for i, d in enumerate(data):
#     assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
#     print(f'Тестовый набор {d} прошёл проверку')
# print('Всё ок')

# val = 391
#
# units = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'VI', 5: 'V', 6: 'IV', 7: 'IIV', 8: 'IIIV', 9: 'XI'}
# dozens = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'LX', 5: 'L', 6: 'XL', 7: 'XXL', 8: 'XXXL', 9: 'CX'}
# hundreds = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'DC', 5: 'D', 6: 'CD', 7: 'CCD', 8: 'CCCD', 9: 'MC'}
#
# roman_str = ''
#
# while val > 0:
#     num = val % 10
#     val //= 10
#     if val > 100:
#         roman_str += 'M' * num
#     elif val >= 10:
#         roman_str += hundreds[num]
#     elif val >= 0:
#         roman_str += dozens[num]
#     else:
#         roman_str += units[num]
#
#     # if val >= 1000:
#     #         roman_str += units[num]
#     # elif val >= 100:
#     #     roman_str += dozens[num]
#     # elif val >= 10:
#     #     roman_str += hundreds[num]
#     # else:
#     #     roman_str += 'M' * num
#     val //= 10
#     print(num, val, roman_str)
# print(roman_str[::-1])
