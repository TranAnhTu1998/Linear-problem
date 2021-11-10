import math


def calculate_volume_cylinder():
    print("Вычисление объема цилиндра.")
    print("Введите исходные данные:")
    r = float(input("радиус основания (см) : "))
    h = float(input("высота цилиндра (см) : "))
    print("Объем цилиндра ", (math.pi * r * r) * h, "см. куб.")
