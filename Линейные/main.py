import sys
from rich.table import Table
from rich.console import Console
from rich import print

from cube import calculate_volume_cube
from cylinder import calculate_volume_cylinder
from purchase import calculate_cost_purchase
console = Console()


def programm(method, title, t_key=False):
    b1 = True
    while (b1):
        str_out = ''
        try:
            method()
        except:
            console.print("Введенная вами строка недействительна,", "произошла ошибока ", sys.exc_info()[0], '!!!!')

        b11 = True
        while (b11):
            contin = console.input("Попробовать ещё раз ? (y/n - д/н)")

            if contin == 'y' or contin == 'Y' or contin == 'д' or contin == 'Д':
                b1 = True
                b11 = False
            elif contin == 'n' or contin == 'N' or contin == 'н' or contin == 'Н':
                b1 = False
                b11 = False
            else:
                console.print("Недействительное значение, попробуйте еще раз!!!")
                b11 = True


def select_method():
    console.print("***Добро пожаловать в программу \"Линейные задачи\" ****")
    table = Table(title="Списоки методы шифра:")
    table.add_column("№", justify="center", style="cyan", no_wrap=True)
    table.add_column("Линейные задачи", style="magenta")

    table.add_row("1", "Программу вычисления объема куба.")
    table.add_row("2", "Программу вычисления объема цилиндра. ")
    table.add_row("3", "Программу вычисления стоимости покупки, состоящей из нескольких тетрадей и карандашей. ")
    table.add_row("4", "Программу вычисления стоимости некоторого количества (по весу) яблок.")
    table.add_row("5", "Программу вычисления сопротивления электрической цепи, состоящей из двух параллельных "
                       "соединенных сопротивлений.")
    table.add_row("6", "Программу вычисления стоимости поездки на автомобиле на дачу (туда и обратно). ")
    table.add_row("e", "Нажмите клавишу \"е or в\", чтобы выйти из програмы.")

    console.print(table)

    select_x = input("Какой номер программы вы выберете ? ")

    sel = select_x

    if sel == '1':
        programm(calculate_volume_cube, "Программу вычисления объема куба.", True)

    elif sel == '2':
        programm(calculate_volume_cylinder, "Вычисление объема цилиндра.", True)

    elif sel == '3':
        programm(calculate_cost_purchase(), "Вычисление стоимости покупки", True)

    elif sel == '4':
        '''method_encod(encode_polybius_square, "Квадрат Полибия", False)'''

    elif sel == 'e' or sel == 'E' or sel == 'в' or sel == 'В':
        exit()

    else:
        console.print(
            "Произошла ошибка. Возможно, вы ввели неправильный номер метода или метод не был разработан "
            "программистом.!!!")


def loop_method():
    while True:
        select_method()


loop_method()
