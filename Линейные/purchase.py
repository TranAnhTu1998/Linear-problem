def calculate_cost_purchase():
    print("Вычисление стоимости покупки.")
    print("Введите исходные данные:")
    ct = float(input("Цена тетради (руб.) : "))
    kt = float(input("Количество тетрадей : "))
    ck = float(input("Цена карандаша (руб.) : "))
    kk = float(input("Количество карандашей : "))
    s = ct * kt + ck * kk
    print("Стоимость покупки:  ", s, "rub")

