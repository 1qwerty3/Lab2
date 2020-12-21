import ctypes
import os
import matplotlib.pyplot as plt
import numpy as np



# Подключаем DLL
c_lib = ctypes.CDLL(r'C:\Users\user\Desktop\Лаба\Максим\2.1\Lib2-1.dll')


# Описываем сигнатуру функции TheFunk
c_lib.TheFunc.argtypes = [ctypes.c_char_p, ctypes.c_double]
c_lib.TheFunc.restype = ctypes.c_double


# Вызываем функцию из библиотеки
def make_dll_call(number: int, lastname: ctypes.c_char_p = b'Khlystov'):

    return c_lib.TheFunc(lastname, ctypes.c_double(number))


# Функция для проверки коэффициентов
def my_func(_a, _b, _c, _x):

    return _a * _x * _x + _b * _x + _c


# Находим значения функции в заданном диапозоне
def find_function_values():

    y_list: list = []
    x_list: list = []
    i = 0

    while i < 11:
        _res = make_dll_call(i)
        x_list.append(i)
        y_list.append(_res)

        i += 0.5

    return x_list, y_list


# Находим коэффициенты
def find_coefs():

    # Три случйаные точки
    x1 = 0
    x2 = 1
    x3 = 2

    # Значения функция для этих точек
    y1 = make_dll_call(x1)
    y2 = make_dll_call(x2)
    y3 = make_dll_call(x3)

    # Составляем матрицы для Крамера
    op1 = np.matrix(f'{x1 * x1} {x1} 1; {x2 * x2} {x2} 1; {x3 * x3} {x3} 1')
    op2 = np.matrix(f'{y1} {x1} 1; {y2} {x2} 1; {y3} {x3} 1')
    op3 = np.matrix(f'{x1 * x1} {y1} 1; {x2 * x2} {y2} 1; {x3 * x3} {y3} 1')
    op4 = np.matrix(f'{x1 * x1} {x1} {y1}; {x2 * x2} {x2} {y2}; {x3 * x3} {x3} {y3}')

    # Ищем коэффиценты с помощью определителей
    _a = np.linalg.det(op2) / np.linalg.det(op1)
    _b = np.linalg.det(op3) / np.linalg.det(op1)
    _c = np.linalg.det(op4) / np.linalg.det(op1)

    return _a, _b, _c


if __name__ == '__main__':
    # Значени X и Y
    x, y = find_function_values()
    # Коэффициенты
    a, b, c = find_coefs()

    # График
    plt.plot(x, y)
    plt.title(f'y={a}x^2 {b}x {c}')
    plt.gca().invert_yaxis()
    plt.xlabel = 'Ось X'
    plt.ylable = 'Ось Y'
    plt.title('')
    plt.show()

    # Проверка коэффициентов
    for x in range(0, 11):
        res = make_dll_call(x)
        my_res = my_func(a, b, c, x)
        print(f'При x={x}:')
        print('Результат из dll: {0:.3g}'.format(res))
        print('Результат исходя из коэффициентов: {0:.3g}'.format(my_res))
        print('\n')
