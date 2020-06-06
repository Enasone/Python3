#A и B и ошибки компиляции
# x = int(input())
# x1 = list(map(int, input().split()))
# x2 = list(map(int, input().split()))
# x3 = list(map(int, input().split()))
#
# res = sum(x1) - sum(x2)
# res2 = sum(x2) - sum(x3)
#
# print(res, '\n', res2, sep='')

# В поисках простой задачи
# x = int(input('Введите кол-во человек которых опросили: '))
# x1 = list(map(int, input('Введите ответы тех людей, которых опросили: ').split()))
# x3 = ["Easy", 'Hard']
#
# res = max(x1)
# print(x3[res])

#Новый год: встреча друзей
# x = list(map(int, input().split()))
#
# x1 = max(x)
# x2 = min(x)
# x3 = (x1+x2) // len(x)
#
# res = (x1 - x3) + (x3 - x2)
# print(res)

#Дефиснутая фраза
# x = input().upper()
#
# x1 = x.split()
#
# q = x1[0].replace('', ' ').split()
# qres = '-'.join(q)
# q1 = x1[1].replace('', ' ').split()
# q1res = '-'.join(q1)
#
# print(qres, q1res)

# #Какое из чисел больше?
#
# x = int(input())
# x1 = int(input())
#
# if x > x1:
#     print("1")
# if x1 > x:
#     print("2")
# if x1 == x:
#     print("0")

#Налог 13%

# x = int(input())
#
# if x > 20000:
#     x1 = (x//100)*13
#     x = x - x1
#     print(x)
# else:
#     print(x)

#Максимум из двух чисел

#1)
# x = int(input())
# x1 = int(input())
#
# res = max(x, x1)
# print(res)

#2)
# x = int(input())
# x1 = int(input())
#
# if x > x1:
#     print(x)
# else:
#     print(x1)

# Четырехзначный падиндром
# x = list(map(int, input().replace('', ' ').split()))
#
# if x[0] == x[3] and x[1] == x[2]:
#     print('YES')
# else:
#     print('NO')

#Арифметика
# x = list(map(int, input().split()))
#
# if x[0] * x[1] == x[2]:
#     print('YES')
# else:
#     print('NO')

#Перевод
# x = input()
# x1 = input()[::-1]
#
# if x == x1:
#     print('YES')
# else:
#     print('NO')

#Ладья
# x = int(input())
# x2 = int(input())
#
# x3 = int(input())
# x4 = int(input())
#
# if ((x > x3 or x < x3) and x2 == x4) or ((x2 > x4 or x2 < x4) and x == x3):
#     print('YES')
# else:
#     print('NO')

#Фубол
# x = input()
#
# if x.count('0') >= 7 or x.count('1') >= 7:
#     print('Dangers')
# else:
#     print('NO')

#Возведение в степень по модулю
# n = int(input())
# m = int(input())
#
# print(m % (2**n))

#Cуществует ли треугольник?
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a + b > c and a + c > b and c + b > a:
#     print('YES')
# else:
#     print('NO')

# Слон
# a = int(input())
# b = int(input())
#
# c = int(input())
# v = int(input())
#
# res = abs(a - c)
# res1 = abs(b - v)
#
# if res == res1:
#     print('YES')
# else:
#     print('NO')

#Выгодный проезд
# n = int(input())
# m = int(input())
# a = int(input())
# b = int(input())
#
# summ = n//m
# sums = n % m
#
# if sums != 0 or :
#     print((summ * b) + (sums * a))
# else:
#     print(summ * b)

# Саша и палочки

# x = int(input())
# y = int(input())
#
# res = x//y
#
# if res%2 == 1 or res == 0:
#     print('YES')
# else:
#     print('NO')

#Шоколадка

# n = int(input())
# m = int(input())
# k = int(input())
#
# if (n * m)//2 < k:
#     print('YES')
# else:
#     print('NO')

#Счастилвый билет

# x = list(map(int, input().replace('', ' ').split()))
#
# mathe = x[0] + x[1] + x[2]
# mathe1 = x[-3] + x[-2] + x[-1]
#
# if mathe == mathe1:
#     print('YES')
# else:
#     print('NO')

# Игра палочками

# n, m = map(int, input().split())
#
# nM = n + m
# res = nM//2
#
# if res % 2 == 0:
#     print('Malvika')
# else:
#     print('Akshat')

#Билеты на метро

# n = int(input())
#
# countRun60 = n//60
# ostatocRun60 = n % 60
#
# countRun10 = ostatocRun60//10
# ostatocRun10 = ostatocRun60 % 10
#
# countRun1 = ostatocRun10//1
# ostatocRun1 = ostatocRun10
#
# if ostatocRun60 >= 35:
#     countRun60 += 1
#     countRun10 = 0
#     countRun1 = 0
#     print(countRun1, countRun10, countRun60)
# elif ostatocRun10 == 9:
#     countRun1 = 0
#     countRun10 += 1
#     print(countRun1, countRun10, countRun60)
# else:
#     print(countRun1, countRun10, countRun60)

#Подсчёт функции
# import math
#
# x = int(input())
#
# res = math.ceil(x/2)
#
# if x % 2 == 1:
#     print('-', res, sep = '')
# else:
#     print(res)

#больше-меньше

# x = int(input())
# x1 = int(input())
#
# if x > x1:
#     print('>')
# else:
#     if x < x1:
#         print('<')
#     else:
#         if x == x1:
#             print('=')

#Максимум из трех

# x1 = int(input())
# x2 = int(input())
# x3 = int(input())

#1)
# res = max(x1, x2, x3)
# print(res)

#2)
# if x1 > x2:
#     if x1 > x3:
#         print(x1)
#     else:
#         print(x3)
# else:
#     if x2 > x1:
#         if x2 > x3:
#             print(x2)
#         else:
#             print(x3)

#Баскетбол

# x1, x2 = map(int, input().split())
# x3, x4 = map(int, input().split())
# x5, x6 = map(int, input().split())
# x7, x8 = map(int, input().split())

#1)
# schet1 = 0
# schet2 = 0
# if x1 > x2:
#     schet1 += 1
# elif x1 < x2:
#     schet2 += 1
# elif x3 > x4:
#     schet1 += 1
# elif x3 < x4:
#     schet2 += 1
# elif x5 > x6:
#     schet1 += 1
# elif x5 < x6:
#     schet2 += 1
# elif x7 > x8:
#     schet1 += 1
# elif x7 < x8:
#     schet2 += 1
# elif schet1 > schet2:
#     print("1")
# else:
#     if schet1 == schet2:
#         print('DRAW')
#     else:
#         print('2')

#2)
# res1 = x1 + x3 + x5 + x7
# res2 = x2 + x4 + x6 + x8
#
# if res1 > res2:
#     print('1')
# else:
#     if res1 < res2:
#         print('2')
#     else:
#         print('DRAW')

#Чет и нечет
# x1 = int(input()) + 1
# x2 = int(input())
# res = []
#
# res.extend(range(x1))
# res.remove(0)
#
# res1 = res[::2]
# res2 = res[1::2]
# res2.sort()
#
# result = res1 + res2
#
# print(result[x2 - 1])

#Восстановление трех числе
# a = list(map(int, input().split()))
# a.sort()
# a1 = a.pop()
#
# res1 = a1 - a[0]
# res2 = a1 - a[1]
# res3 = a1 - a[2]
#
# print(res1, res2, res3)

#Светофор
# x1 = input()
# x2 = input()
# x3 = input()
#
# mas = ['black', 'green', 'yellow', 'red']
#
# if x1 == mas[0] and x2 == mas[0] and (x3 == mas[1] or x3 == mas[1].upper()):
#     print(x1, x2, x3.upper(), sep='\n')
# elif x1 == mas[0] and (x2 == mas[2] or x2 == mas[2].upper()) and x3 == mas[0]:
#     print(x1, x2.upper(), x3, sep='\n')
# elif (x1 == mas[3] or x1 == mas[3].upper()) and x2 == mas[0] and x3 == mas[0]:
#     print(x1.upper(), x2, x3, sep='\n')
# elif (x1 == mas[3] or x1 == mas[3].upper()) and (x2 == mas[2] or x2 == mas[2].upper()) and x3 == mas[0]:
#     print(x1.upper(), x2.upper(), x3, sep='\n')
# else:
#     print('ERROR')

#Ряд чисел
# i = 50
#
# while i <= 150:
#     print(i)
#     i += 1

#Ряд числе 2
# i = 13
#
# while i <= 349:
#     print(i)
#     i += 7

#Поехали
# i = 15
#
# while i >= 0:
#     print(i)
#     i -= 1
# print('POEHALI')

# Я последняя буква в Алфавите

# i = input()
#
# while i[0] == 'Я' or i[0] == 'я':
#     i = input()
# print('END')

#Список квадратов
# x = int(input())
# i = 1
#
# while i ** 2 <= x:
#     print(i ** 2)
#     i += 1

#Утренняя пробежка
# x = int(input())
# x1 = int(input())
# count = 1
#
# while x <= x1:
#     x = x + ((x * 10) / 100)
#     count +=1
# print(count)

#Мишка и старший брат
# x, x1 = map(int, input().split())
# count = 0
#
# while x <= x1:
#     x *= 3
#     x1 *= 2
#     count += 1
# print(count)

#Дело о нулях и единцах
# x = int(input())
# x3 = input().replace('', ' ').split()
# count = 0
#
# while count < x:
#     count += 1
#     if '1' in x3:
#         if '0' in x3:
#             x3.remove('1')
#             x3.remove('0')
# print(len(x3))

#3иминй вечер в Бурсе
# x = input()
#
# while x[0] != '1':
#     x1 = x[0]
#     x2 = x[::1]
#     x = int(x1) * int(x2)
#     x = str(x)
# print(x)

#Вася и носки
# x = int(input())
# x1 = int(input())
#
# xx = x1
# count = 0
#
# while x != 0:
#     x -= 1
#     count += 1
#     if x1 == count:
#         count += 1
#         x1 = x1 + xx
#
# print(count)

#Новый год и спешка

# x, x1 = map(int, input().split())
# count = 0

# while x != count and x1 < 240:
#     count += 1
#     x1 = x1 + count * 5
#     if x1 > 240:
#         count -= 1
# print(count)

#Новогодние свечки

# x, x1 = map(int, input().split())
# xx = x

# while xx > 1:
#     xx = xx // x1
#     x = x + xx
# print(x)

# Система уравнений

#1)
# n, m = map(int, input().split())

# a, b = 0, -1
# res = 0
# res2 = 0
# result = []
# count = 0

# while res2 <= 300:
#     res2 += 1
#     b += 1
#     a = 0
#     res = 0
#     while res < n:
#         a += 1
#         res = a ** 2 + b
#         if res == n:
#             result.append(a)
#             result.append(b)
#             if result[0] + result[1] ** 2 == m:
#                 count += 1
#                 res = 0
#                 result.clear()
#             else:
#                 res = 0
#                 result.clear()
# print(count)

#2)
# print('Введите n и m:') #a**2+b=n
# n, m = map(int,input().split()) #a+b**2=m
# a = int(1)
# b = int(1)
# count = int()

# while a**2 < n:
#     a += 1
#     b = n-a**2
#     if a >= 0 and b >= 0 and a+b**2 == m:
#         count += 1
# print(count)

#Ваня и кубики

# x = int(input())
#
# x1 = int(0)
# x2 = int(0)
# x3 = int(0)
#
# count = 0
#
# while x3 <= x:
#     x1 += 1
#     x2 = x2 + x1
#     x3 = x2 + x3
#
#     count += 1
#
# print(count - 1)

#Бал в БерлГУ
x = int(input())
x1 = list(map(int, input().split()))
z = int(input())
z1 = list(map(int, input().split()))

# i = 0
# v = -1
# count = 0
#
# while i <= x+z:
#     v += 1
#     c = 0
#     i += 1
#     while x1[c] != x1[-1]:
#         res0 = x1[c]
#         res1 = x1[c] - 1
#         res2 = x1[c] + 1
#         c += 1
#         if res0 == z1[v] or res1 == z1[v] or res2 ==z1[v]:
#             if z1[v] == z1[-1]:
#                 v = 0
#             count += 1
#             z1.remove(z1[v])
#             x1.remove(x1[c])
# print(count)
