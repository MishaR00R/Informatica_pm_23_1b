import math
from math import *


def task1():
    x = float(input("введите переменную a="))
    y = float(input("введите переменную y="))
    z = float(input("введите переменную z="))
    a = abs(x**(1/5))+sin(y)/1+tan(x)-log10(1+y)
    if x <= 0:
        print("ошибка")
        exit(0)
    b = log(x) - (y ** (1 / 3)) - (abs(x ** (1 / 3)) + (z ** (1 / 4)))
    print("a {:.4f}, b {:.4f}".format(a,b))


def task2():
    x = float(input("Введите число х = "))
    a = 2
    b = -1

    if (x + a) == 0:
        print("ошибка")
        exit(0)
    f = ((x**3)**1/4)/(x+a) + x**b

    print("f(x) = {:.4f}".format(f))


def task3():
    x = float(input("введите x : "))
    xs = x ** (1/2)
    f = (sinh(xs))+(cosh(xs))

    print("f(x) = {:.4f}".format(f))


def task4():
    r = float(input("введите r ="))
    R = float(input("введите R ="))
    h = float(input("введите h ="))

    area = math.pi * (R ** 2 - r ** 2) * h

    print("Площадь кольца равна:", area)


def task5():
    v1 = float(input("Введите скорость первого автомобиля (км/ч): "))
    v2 = float(input("Введите скорость второго автомобиля (км/ч): "))
    s = float(input("Введите расстояние между автомобилями (км): "))
    t = float(input("Введите время (часы): "))

    total_distance = s + (v1 + v2) * t

    print(f"Расстояние между автомобилями через {t} часов: {total_distance} км.")


def task6():

    R = float(input("введите R:\n")) # \n - перенос строки
    r = float(input("введите r:\n"))
    l = float(input("введите l:\n"))
    L = float(input("введите L:\n"))
    if L == 0:
        print("ошибка")
        exit(0)
    S= (math.pi * (R ** 2 + r ** 2 + R * r) * l) / (2 * L)

    print(f"Площадь вертикального сечения: ", "{:.4f}".format(S))


def task7():
    x1 = float(input("ведите x1:"))
    x2 = float(input("ведите x2:"))
    distance = abs(x2 - x1)
    print("расстояние между 2 точками ", distance)


def task8():

    u1 = float(input("Введите скорость колонны в км/ч: "))
    L = float(input("Введите расстояние между отрядами в метрах: "))

    if u1 == 0:
        print("ошибка")
        exit(0)
    t1 = L / u1
    t = 2 * t1
    print("Время, через которое велосипедист вернулся обратно:", t)


def task9():

    amount=float(input("Введите сумму - "))

    commission_rate = 0.05  # 5% комиссия
    exchange_rate = 6.5  # курс обмена 1 доллар = 6.5 юаней

    commission = amount * commission_rate
    converted_amount = (amount - commission) * exchange_rate

    print(f"{amount} $ = ", "{:.2f}".format(converted_amount))

task9()
