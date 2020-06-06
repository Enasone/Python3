#  Хипстер Вася
# a = int(input())
# b = int(input())
#
# x2 = abs((a - b)) // 2
# x = (abs(a+b)-abs(a-b)) // 2
# print(x,x2)

#Электонные часы
# second = int(input())
#
# hour = second//60//60%24
# mint = second//60%60
# sec = second%60
#
# print("{}:{:02d}:{:02d}".format(hour,mint,sec))

#Мкад
# v = int(input())
# t = int(input())
#
# res = abs(v*t) - 109
# print(abs(res))

#Парты (trunc, floor, ceil)
# import math
#
# x1 = int(input())
# x2 = int(input())
# x3 = int(input())
#
# q = math.ceil((x1+x2+x3)/2)
#
# print(q)

#Проверка на положительность
# x = int(input())
# x2 = int(input())
# x3 = int(input())
#
# res = bool(x > 0)
# res1 = bool(x2 > 0)
# res2 = bool(x3 > 0)
#
# print('\n', res, '\n', res1, '\n', res2)

#Проверка на честность
# x = int(input())
# x2 = int(input())
# x3 = int(input())
# x4 = int(input())
#
# res = x%2 == 0
# res2 = x2%2 == 0
# res3 = x3%2 == 0
# res4 = x4%2 == 0
#
# print(res, res2, res3 , res4, sep = '\n')

#Проверка числа на кратность 6
# x = int(input())
# xx = int(input())
#
# res = x%6 == 0
# ress = xx%6 == 0
#
# print(res,ress)

#Число не кратно 9 ?
# x = int(input())
# xx = int(input())
# xxx = int(input())
#
# res = x%9 != 0
# ress = xx%9 != 0
# resss = xxx%9 != 0
#
# print(res,ress,resss, sep = '\n')

#Последняя Цифра Числа 2 ?
# x = int(input())
# xx = int(input())
#
# res = x%10 == 2
# ress = xx%10 == 2
#
# print(res, ress)

#Оба числа делятся на 7
# x,xx = int(input()), int(input())
# x1,x2 = int(input()), int(input())
# x3,x4 = int(input()), int(input())
#
# res1 = x%7 == 0 and xx%7 == 0
# res2 = x1%7 == 0 and x2%7 == 0
# res3 = x3%7 == 0 and x4%7 == 0
#
# print(res1, res2, res3)

#Треугольник правильный?
# x = int(input())
# x1 = int(input())
# x2 = int(input())
#
# res = x == x1 == x2
# print(res)

#Условие задачи
# x = int(input())
#
# res = x > 5 and x <= 19
# print(res)

#Хотя бы одно делится на 4
# x = int(input())
# x1 = int(input())
#
# res = x%4 == 0 or x1%4 == 0
# print(res)

#Треугольник равнобедренный?
# a = int(input())
# b = int(input())
# c = int(input())
#
# res = a == b or a == c or b == c
# print(res)

#Число двузначное?
# x = int(input())
#
# res = x >= 10 and x < 100
# print(res)

#Треугольник Прямоугольный?
# a = int(input())
# b = int(input())
# c = int(input())
#
# res = a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2
# print(res)

#Я стану крутым программистом!
# b = 'Я стану крутым программистом! \n'
#
# print(b * 3)

# Повтори 2 фразы
# x = input()
# a = input()
#
# res = x + '\n' + a
# print(res)

#Повтори 3 фразы
# x = input()
# a = input()
# b = input()
#
# res = b + '\n' + a + '\n'
# print(res)

#Повтор строки
# x = input() + " "
#
# res = x * 4
# print(res)

#Длина строки
# x = input()
#
# res = len(x)
# print(res)

#Конкатенация
# x = input()
# r = input()
#
# print(x + r)

#Дублирование строки
# x = input()
#
# print(x*3)

#Классика жанра
# print('Лев Николаевич Толстой написал "' + "Война и мир'")

#Делаем срезу

# s = 'Abrakadabra'
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[-1::-2])
# print(len(s))

#Найти сумму первой и последней цифры числа

# s = input()
#
# print(int(s[0]) + int(s[-1]))

#Две половинки
# import math
# s = input()
#
# x = len(s)
# x1 = math.ceil(x/2)
# res = s[x1:] + s[:x1]
# print(res)

#Кол-во слов

#1)
# x = 'Hello world'
#
# v = x.count('Hello')
# z = x.count('world')
# print(v+z)

#2)
# x = input()
#
# x = x.count(' ')
# print(x + 1)

#3) - Pravilnoe !!!
# x = input()
#
# x = x.split()
# print(len(x))

#Defanging an IP Address

# address = input()
#
# address = address.replace('.', '[.]')
# print(address)

#Удаление символа

# clearSimvol = input()
#
# clearSimvol = clearSimvol.replace('@', '')
# print(clearSimvol)

#Вставка символов

# 1) Первое решение
# x = input()

# x = x.replace('', '*')
# x = x[1:-1]
# print(x)

# 2) Второе решение
# x = input()

# x = x.replace('', ' ').split()
# x = '*'.join(x)
# print(x)

# 3) Третье решение
# x = input()
#
# x = x.replace('', '*')
# x = x.strip('*')
# print(x)

#A. Капитализация слова

# upp = input()
#
# upp1 = upp[0].upper()
# upp2 = upp[1::]
# print(upp1 + upp2)

#A. Упражнение на строки

# 1) Вариант первый
# dem = input()
#
# dem = dem.lower()
# dem = dem.replace('a', '')
# dem = dem.replace('o', '')
# dem = dem.replace('y', '')
# dem = dem.replace('e', '')
# dem = dem.replace('u', '')
# dem = dem.replace('i', '')
# dem = dem.replace('', '.').rstrip('.')
# print(dem)

# 2) Вариант второй
# dem = input()
#
# dem = dem.lower()
# dem = dem.replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
# dem = dem.replace('', '.').rstrip('.')
# print(dem)

#Чат

# x = input()
#
# x1 = x.rfind('h')
#
# x2 = x[x1 + 1] == 'e'
# res = x.rfind('e')
#
# x3 = x[res + 1] == 'l'
# res1 = x.find('l')
#
# x4 = x[res1 + 1] == 'l'
# res2 = x.rfind('l')
#
# x5 = x[res2 + 1] == 'o'
#
# x6 = x2 and x3 and x4 and x5
#
# if x6 == True:
#     print('Yes')
# else:
#     print('NO')

#Первое и последнее вхождение

# x = input()
# finds = input()
#
# x1 = x.find(finds)
# x2 = x.rfind(finds)
# if x2 != x1:
#     print(x1, x2)
# else:
#     print(x1)

# Удаление фрагмента

# x = input()
#
# rez = x[:x.find('h')].rfind(' ')
#
# res = x[:rez], x[x.rfind('h'):]
# res2 = ' '.join(res)
#
# print(res2)

#Переставить два слова

#1)
# x = input()
#
# x = x.split()
# print(x[1], x[0])

#2)
# s = input()
# a, b = s.split()
# print(b, a)

#Второе вхождение

# x = input()
#
# x1 = x.find('f')
# x2 = x.rfind('f')
#
# if x2 != x1:
#     print(x2)
# elif x2 == x1:
#     print('-1')
# else:
#     print('-2')

#A. Дабстеп

# x = input()
#
# x = x.replace('WUB', ' ')
# x = x.split()
# x = ' '.join(x)
# print(x)

#Карточки

# chislo = int(input('Введите число карточке: '))
# stroka = input('Введите буквы: ')
#
# z = stroka.count('z')
# e = stroka.count('e')
# r = stroka.count('r')
# o = stroka.count('o')
# n = stroka.count('n')
#
# while o and n and e != 0:
#     print('1')
#     o -= 1
#     n -= 1
#     e -= 1
# while z and e and r and o != 0:
#     print('0')
#     z -= 1
#     e -= 1
#     r -= 1
#     o -= 1
