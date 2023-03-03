"""This program is a calculator for calculating an expression of the type: a (op) b = c
The expression and the result are output both in mathematical form
and in written words.
a, b are positive integers.
0 <= a <= 999, 0 <= b <= 999, 0 <= c <= 99,999
po operations (*, +, -, /), integer division"""



"""Эта программа-калькулятор для вычисления выражения типа: a (op) b = c
Выражение и результат выводится как в математическом виде,
так и письменно прописью.
a, b - целые положительные числа.
0 <= a <= 999, 0 <= b <= 999, 0 <= c <= 99 999
po - операции (*, +, -, /), деление целочисленное"""


def voice_num():
    dc = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять',
          '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', '0': 'ноль'}
    dc1 = {'10': 'десять', '11': 'одиннадцать', '12': 'двенадцать',
           '13': 'тринадцать', '14': 'четырнадцать', '15': 'пятнадцать',
           '16': 'шестнадцать', '17': 'семнадцать', '18': 'восемнадцать',
           '19': 'девятнадцать'}
    dc_10 = {'2': 'двадцать', '3': 'тридцать', '4': 'сорок',
             '5': 'пятьдесят',
             '6': 'шестьдесят', '7': 'семьдесят', '8': 'восемьдесят',
             '9': 'девяносто', '0': 'ноль', '20': 'двадцать', '30': 'тридцать',
             '40': 'сорок', '50': 'пятьдесят',
             '60': 'шестьдесят', '70': 'семьдесят', '80': 'восемьдесят',
             '90': 'девяносто', '00': 'ноль'}
    dc_100 = {'1': 'сто', '2': 'двести', '3': 'триста', '4': 'четыреста',
              '5': 'пятьсот', '6': 'шестьсот', '7': 'семьсот', '8': 'восемьсот',
              '9': 'девятьсот', '0': 'ноль'}
    dc_1k = {'1': 'одна тысяча', '2': 'две тысячи', '3': 'три тысячи',
             '4': 'четыре тысячи', '5': 'пять тысяч', '6': 'шесть тысяч',
             '7': 'семь тысяч', '8': 'восемь тысяч', '9': 'девять тысяч'}
    lst1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    t = 'тысяч'

    print()
    print('Эта программа-калькулятор для вычисления выражения типа: a (op) b = c')
    print('Выражение и результат выводится как в математическом виде,\nтак'
          ' и письменно прописью.')
    print('a, b - целые положительные числа.')
    print('0 <= a <= 999, 0 <= b <= 999, 0 <= c <= 99 999')
    print('po - операции (*, +, -, /), деление целочисленное')

    input_miss = 'Ошибка ввода!\nДопустимо: 0 <= a <= 999  и  0 <= b <= 999'
    input_miss_op = 'Ошибка ввода! Допустимы цифры и знак операции (*, +, -, /).'
    input_miss_len = 'Ошибка ввода! Превышено значение результата: ' \
                     '0 <= c <= 99 999.\nВведите меньшие значения <а>  и/или  <b>.'

    ext = 'None'
    while ext != 'n':
        while True:
            print()
            st = input(f'Введите выражение: ')
            st = st.replace(' ', '')
            if '*' in st and st.count('*') == 1:
                st = st.split('*')
                if st[0].isdigit() and st[1].isdigit() and 1 <= len(st[0]) <= 3 and\
                        1 <= len(st[1]) <= 3:
                    rez = int(st[0]) * int(st[1])
                    oper = 'умножить на'
                    z = '*'
                    rez_st = str(rez)
                    if len(rez_st) <= 5:
                        break
                    else:
                        print(input_miss_len)
                else:
                    print(input_miss)

            elif '+' in st and st.count('+') == 1:
                st = st.split('+')
                if st[0].isdigit() and st[1].isdigit() and 1 <= len(st[0]) <= 3 and\
                        1 <= len(st[1]) <= 3:
                    rez = int(st[0]) + int(st[1])
                    rez_st = str(rez)
                    oper = 'плюс'
                    z = '+'
                    if len(rez_st) <= 5:
                        break
                    else:
                        print(input_miss_len)
                else:
                    print(input_miss)

            elif '-' in st and st.count('*') == 1:
                if st[0].isdigit() and st[1].isdigit() and 1 <= len(st[0]) <= 3 and\
                        1 <= len(st[1]) <= 3:
                    st = st.split('-')
                    rez = int(st[0]) - int(st[1])
                    rez_st = str(rez)
                    oper = 'минус'
                    z = '-'
                    if len(rez_st) <= 5:
                        break
                    else:
                        print(input_miss_len)
                else:
                    print(input_miss)

            elif '/' in st and st.count('*') == 1:
                if st[0].isdigit() and st[1].isdigit() and 1 <= len(st[0]) <= 3 and\
                        1 <= len(st[1]) <= 3 and st[1] != 0:
                    st = st.split('/')
                    rez = int(int(st[0]) / int(st[1]))
                    rez_st = str(rez)
                    oper = 'разделить на'
                    z = ':'
                    if len(rez_st) <= 5:
                        break
                    else:
                        print(input_miss_len)
                if st[1] == 0:
                    print('Ошибка! Делить на <0> нельзя.')
                else:
                    break
            else:
                print(input_miss_op)

        if int(st[0]) in lst1:
            a = dc1[st[0]]
        if int(st[1]) in lst1:
            b = dc1[st[1]]
        if int(rez_st) in lst1:
            c = dc1[rez_st]

        if len(st[0]) == 1:
            a = dc[st[0]]
        if len(st[1]) == 1:
            b = dc[st[1]]
        if len(rez_st) == 1:
            c = dc[rez_st]

        if len(st[0]) == 2 and int(st[0]) not in lst1:
            if st[0][1] == '0':
                a = dc_10[st[0][0]]
            if st[0][1] != '0':
                a = dc_10[st[0][0]] + ' ' + dc[st[0][1]]

        if len(st[1]) == 2 and int(st[1]) not in lst1:
            if st[1][1] == '0':
                b = dc_10[st[1][0]]
            if st[1][1] != '0':
                b = dc_10[st[1][0]] + ' ' + dc[st[1][1]]

        if len(rez_st) == 2 and int(rez_st) not in lst1:
            if rez_st[1] == 0:
                c = dc_10[rez_st[0]]
            else:
                c = dc_10[rez_st[0]] + ' ' + dc[rez_st[1]]

        if len(st[0]) == 3:
            try:
                if st[0][1] == '0' and st[0][2] != '0' and int(st[0][1:]) not in lst1:
                    a = dc_100[st[0][0]] + ' ' + dc[st[0][2]]
                if int(st[0][1:]) in lst1:
                    a = dc_100[st[0][0]] + ' ' + dc1[st[0][1:]]
                if st[0][1] == '0' and st[0][2] == '0' and int(st[0][1:]) not in lst1:
                    a = dc_100[st[0][0]]
                if st[0][1] != '0' and st[0][2] == '0' and int(st[0][1:]) not in lst1:
                    a = dc_100[st[0][0]] + ' ' + dc_10[st[0][1]]
                if st[0][1] != '0' and st[0][2] != '0' and int(st[0][1:]) not in lst1:
                    a = dc_100[st[0][0]] + ' ' + dc_10[st[0][1]] + ' ' + dc[st[0][2]]
            except KeyError:
                print()
                print(f'Внутренняя ошибка: неверный ключ словаря!\n'
                      f'Попробуйте с другими цифрами.')
                print()

        if len(st[1]) == 3:
            try:
                if st[1][1] == '0' and st[1][2] != '0' and int(st[1][1:]) not in lst1:
                    b = dc_100[st[1][0]] + ' ' + dc[st[1][2]]
                if int(st[1][1:]) in lst1:
                    b = dc_100[st[1][0]] + ' ' + dc1[st[1][1:]]
                if st[1][1] == '0' and st[1][2] == '0':
                    b = dc_100[st[1][0]]
                if st[1][1] != '0' and st[1][2] == '0' and int(st[1][1:]) not in lst1:
                    b = dc_100[st[1][0]] + ' ' + dc_10[st[1][1]]
                if st[1][1] != '0' and st[1][2] != '0' and int(st[1][1:]) not in lst1:
                    b = dc_100[st[1][0]] + ' ' + dc_10[st[1][1]] + ' ' + dc[st[1][2]]
            except KeyError:
                print()
                print(f'Внутренняя ошибка: неверный ключ словаря!\n'
                      f'Попробуйте с другими цифрами.')
                print()

        if len(rez_st) == 3:
            try:
                if rez_st[1] == '0' and rez_st[2] != '0' and \
                        int(rez_st[1:]) not in lst1:
                    c = dc_100[rez_st[0]] + ' ' + dc[rez_st[2]]
                if int(rez_st[1:]) in lst1:
                    c = dc_100[rez_st[0]] + ' ' + dc1[rez_st[1:]]
                if rez_st[2] == '0' and int(rez_st[1:]) not in lst1:
                    c = dc_100[rez_st[0]] + ' ' + dc_10[rez_st[1]]
                if rez_st[1] == '0' and rez_st[2] == '0' and int(rez_st[1:]) not in lst1:
                    c = dc_100[rez_st[0]]
                if rez_st[1] != '0' and rez_st[2] != '0' and int(rez_st[1:]) not in lst1:
                    c = dc_100[rez_st[0]] + ' ' + dc_10[rez_st[1]] + ' ' + dc[rez_st[2]]
            except KeyError:
                print()
                print(f'Внутренняя ошибка: неверный ключ словаря!\n'
                      f'Попробуйте с другими цифрами.')
                print()

        if len(rez_st) == 4:
            try:
                if rez_st[1] != '0' and rez_st[2] != '0' and rez_st[3] == '0' \
                        and int(rez_st[2:]) in lst1:
                    c = dc_1k[rez_st[0]] + ' ' + dc_100[rez_st[1]] + ' ' + \
                         dc1[(rez_st[2:])]
                if rez_st[1] == '0' and rez_st[2] != '0' and rez_st[3] != '0' \
                        and int(rez_st[2:]) not in lst1:
                    c = dc_1k[rez_st[0]] + ' ' + dc_10[rez_st[2]] + ' ' + dc[rez_st[3]]
                if int(rez_st[2:]) in lst1 and rez_st[1] == '0' and rez_st[2] != '0':
                    c = dc_1k[rez_st[0]] + ' ' + dc1[rez_st[2:]]
                if rez_st[1] == '0' and rez_st[2] == '0'\
                        and rez_st[3] != '0' and int(rez_st[2:]) not in lst1:
                    c = dc_1k[rez_st[0]] + ' ' + dc[rez_st[3]]
                if rez_st[1] == '0' and rez_st[2] != '0'\
                        and rez_st[3] == '0' and int(rez_st[2:]) not in lst1:
                    c = dc_1k[rez_st[0]] + ' ' + dc_10[rez_st[2]]
                if int(rez_st[2:]) in lst1 and rez_st[1] != '0' and rez_st[2] != '0':
                    c = dc_1k[rez_st[0]] + ' ' + dc_100[rez_st[1]] + ' ' + dc1[rez_st[2:]]
                if rez_st[1] != '0' and rez_st[2] == '0' and rez_st[3] != '0':
                    c = dc_1k[rez_st[0]] + ' ' + dc_100[rez_st[1]] + ' ' + dc[rez_st[3]]
                if rez_st[1] != '0' and rez_st[2] != '0'\
                        and rez_st[3] != '0' and int(rez_st[2:]) not in lst1:
                    c = dc_1k[rez_st[0]] + ' ' + dc_100[rez_st[1]] + ' ' + \
                            dc_10[rez_st[2]] + ' ' + dc[rez_st[3]]
                if rez_st[1] != '0' and rez_st[2] != '0' and rez_st[3] == '0' and\
                        int(rez_st[2:]) not in lst1:
                    c = dc_1k[rez_st[0]] + ' ' + dc_100[rez_st[1]] + ' ' + \
                            dc_10[rez_st[2]]
                if rez_st[1] != '0' and rez_st[2] == '0' and rez_st[3] == '0':
                    c = dc_1k[rez_st[0]] + ' ' + dc_100[rez_st[1]]
                if rez_st[1] == '0' and rez_st[2] == '0' and rez_st[3] == '0':
                    c = dc_1k[rez_st[0]]
            except KeyError:
                print()
                print(f'Внутренняя ошибка: неверный ключ словаря!\n'
                      f'Попробуйте с другими цифрами.')
                print()

        if len(rez_st) == 5:
            try:
                if int(rez_st[0:2]) not in lst1 and rez_st[1] == '0' and rez_st[2] != '0' and\
                        rez_st[3] != '0' and rez_st[4] == '0' and int(rez_st[3:]) not in lst1:
                    c = dc_10[rez_st[0]] + ' ' + t + ' ' + dc_100[rez_st[2]] + ' ' + \
                        dc_10[rez_st[3]]
                if int(rez_st[0:2]) not in lst1 and rez_st[1] == '0' and rez_st[2] != '0' and\
                        rez_st[3] != '0' and rez_st[4] != '0' and int(rez_st[3:]) not in lst1:
                    c = dc_10[rez_st[0]] + ' ' + t + ' ' + dc_100[rez_st[2]] + ' ' + \
                        dc_10[rez_st[3]] + ' ' + dc[rez_st[4]]
                if int(rez_st[0:2]) not in lst1 and rez_st[2] == '0' and rez_st[3] != '0' \
                         and int(rez_st[3:]) in lst1:
                    c = dc_10[rez_st[0]] + ' ' + dc_1k[rez_st[1]] + ' ' + dc1[rez_st[3:]]
                if int(rez_st[0:2]) not in lst1 and rez_st[2] != '0' and \
                        rez_st[3] != '0' and int(rez_st[3:]) in lst1:
                    c = dc_10[rez_st[0]] + ' ' + dc_1k[rez_st[1]] + ' ' + \
                        dc_100[rez_st[2]] + ' ' + dc1[rez_st[3:]]
                if int(rez_st[0:2]) not in lst1 and rez_st[1] != '0' and rez_st[2] != '0'\
                        and rez_st[3] == '0' and rez_st[4] != '0':
                    c = dc_10[rez_st[0]] + ' ' + dc_1k[rez_st[1]] + ' ' + \
                        dc_100[rez_st[2]] + ' ' + dc[rez_st[4]]
                if int(rez_st[0:2]) not in lst1 and rez_st[1] != '0' and rez_st[2] != '0'\
                        and rez_st[3] != '0' and rez_st[4] == '0' and \
                        int(rez_st[3:]) not in lst1:
                    c = dc_10[rez_st[0]] + ' ' + dc_1k[rez_st[1]] + ' ' + \
                        dc_100[rez_st[2]] + ' ' + dc_10[rez_st[3]]
                if int(rez_st[0:2]) not in lst1 and rez_st[1] == '0'and rez_st[2] == '0'\
                        and rez_st[3] == '0' and rez_st[4] == '0':
                    c = dc_10[rez_st[0]] + ' ' + t
                if int(rez_st[0:2]) not in lst1 and rez_st[2] != '0' and\
                        rez_st[3] == '0' and rez_st[4] == '0':
                    c = dc_10[rez_st[0]] + ' ' + dc_1k[rez_st[1]] + ' ' + \
                            dc_100[rez_st[2]]
                if int(rez_st[0:2]) not in lst1 and rez_st[1] != '0'and rez_st[2] != '0' and\
                        rez_st[3] != '0' and rez_st[4] != '0' and int(rez_st[3:]) not in lst1:
                    c = dc_10[rez_st[0]] + ' ' + dc_1k[rez_st[1]] + ' ' + \
                            dc_100[rez_st[2]] + ' ' + dc_10[rez_st[3]] + ' ' + dc[rez_st[4]]
                if int(rez_st[0:2]) in lst1 and rez_st[2] != '0' and rez_st[3] != '0' \
                        and rez_st[4] == '0' and int(rez_st[3:]) in lst1:
                    c = dc1[rez_st[0:2]] + ' ' + t + ' ' + dc_100[rez_st[2]] + ' ' + \
                        dc1[rez_st[3:]]
                if int(rez_st[0:2]) in lst1 and rez_st[2] != '0' and rez_st[3] == '0' \
                        and rez_st[4] == '0' and int(rez_st[3:]) not in lst1:
                    c = dc1[rez_st[0:2]] + ' ' + t + ' ' + dc_100[rez_st[2]]
                if int(rez_st[0:2]) in lst1 and rez_st[2] != '0' and rez_st[3] != '0' \
                        and rez_st[4] == '0' and int(rez_st[3:]) not in lst1:
                    c = dc1[rez_st[0:2]] + ' ' + t + ' ' + dc_100[rez_st[2]] + ' ' +\
                        dc_10[rez_st[3]]
                if int(rez_st[0:2]) in lst1 and rez_st[2] != '0' and rez_st[3] != '0' and\
                        rez_st[4] != '0':
                    c = dc1[rez_st[0:2]] + ' ' + t + ' ' + dc_100[rez_st[2]] + ' ' + \
                            dc_10[rez_st[3]] + ' ' + dc[rez_st[4]]
            except KeyError:
                print()
                print(f'Внутренняя ошибка: неверный ключ словаря!\n'
                      f'Попробуйте с другими цифрами.')
                print()

        try:
            print(f'Выражение: {st[0]} {z} {st[1]} = {rez_st}')
            print(f'Результат: {a} {oper} {b} равно {c}.')
            print()
            ext = input('Для ПРОДОЛЖЕНИЯ нажмите <любую букву>, для ВЫХОДА <n>: ')
        except UnboundLocalError:
            print()
            print(f'Внутренняя ошибка: переменная <с> не определена!\n'
                  f'Попробуйте с другими цифрами.')
            print()
    print()
    print('*** Программа-калькулятор выражений ЗАКРЫТА! *** ')


if __name__ == '__main__':
    voice_num()