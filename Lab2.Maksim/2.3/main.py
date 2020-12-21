import ctypes
import matplotlib.pyplot as plt
import os



# Имена файлов с библиотеками
DLLS = [
    'Lib.dll',
    'Lib2-2-1.dll',
    'Lib2-2-2.dll',
    'Lib2-2-3.dll',
    'Lib2-2-3-1.dll',
    'Lib2-2-3-2.dll',
    'MyDLL.dll',
]


# Проверяем функции на работоспособность
def dll_work(_item):

    try:
        ctypes.CDLL(os.path.join(r'C:\Users\user\Desktop\Лаба\Максим\2.3\dll', _item))
    except OSError:
        print(f'Библиотеку {_item} загрузить не удалось')
        return False
    else:
        print(f'Библиотека {_item} успешно загружена')
        return True


# Загружаем библиотеку
def dll_connection(_item):

    return ctypes.CDLL(os.path.join(r'C:\Users\user\Desktop\Лаба\Максим\2.3\dll', _item))


# Ищем значения для графика
def make_data_for_graphic(_item):

    try:
        func_name = _item.FuncName
        the_func = _item.TheFunc
    except AttributeError:
        print('Функция в данной библиотеке повреждена')
        return

    func_name.restype = ctypes.c_char_p

    the_func.argtype = ctypes.c_double
    the_func.restype = ctypes.c_double

    name = func_name().decode('ascii')

    x, y = [], []

    for _i in range(11):
        x.append(_i)
        y.append(the_func(ctypes.c_double(_i)))

    draw_graphic(x, y, name)


# Рисуем график
def draw_graphic(x, y, name):

    plt.figure(figsize=(15, 8))
    plt.plot(x, y)
    plt.xticks(x)
    plt.yticks(y)
    plt.ylable = 'Ось Y'
    plt.title(name)
    plt.show()


if __name__ == '__main__':
    print('Начинаем загрузку библиотек')
    active_dll_list = list(filter(dll_work, DLLS))
    print('Процесс загрузки библиотек завершен')

    make_dll_connection_list = list(map(dll_connection, active_dll_list))

    while True:
        print('Пожалуйста, выберете для какой библиотеки просчитать функцию:')
        for i, item in enumerate(active_dll_list):
            print(f'\t{i+1}.) {item};')
        print('\tДля выхода нажмите любую другую кнопку...')
        choise = int(input())
        if choise in [1, 2, 3, 4, 5, 6]:
            make_data_for_graphic(make_dll_connection_list[choise-1])
        else:
            break
