import numpy as np
from PIL import Image
import csv


def make_field(size):
    field = np.ndarray((size, size), dtype=np.int8)
    field.fill(0)
    field[::2, ::2] = 1
    field[1::2, 1::2] = 1
    return field


def super_sort(rows, cols):
    A = np.random.randint(1, 100, size=(rows, cols))
    B = A.copy()
    B[::2].sort()
    B[1::2, ::-1].sort()
    return (A, B)


def bw_convert(path):
    image = np.asarray(Image.open(path))
    image[:, :, 0] = np.round(image[:, :, 0] * 0.2989)
    image[:, :, 1] = np.round(image[:, :, 1] * 0.5870)
    image[:, :, 2] = np.round(image[:, :, 2] * 0.1140)

    image[:, :, 0] += image[:, :, 1]
    image[:, :, 0] += image[:, :, 2]
    image[:, :, 1] = image[:, :, 0]
    image[:, :, 2] = image[:, :, 0]

    Image.fromarray(np.uint8(image)).save('result.jpg')


cyrillicchars = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']


def cyrillic_to_latin(char):
    if char.lower() not in cyrillicchars:
        return char

    res = str()
    res2 = ''
    if char.lower() == 'й':
        res = 'j'
    elif char.lower() == 'ц':
        res = 'с'
    elif char.lower() == 'у':
        res = 'u'
    elif char.lower() == 'к':
        res = 'k'
    elif char.lower() == 'е':
        res = 'e'
    elif char.lower() == 'н':
        res = 'n'
    elif char.lower() == 'г':
        res = 'g'
    elif char.lower() == 'ш':
        res = 's'
        res2 = 'h'
    elif char.lower() == 'щ':
        res = 's'
        res2 = 'hh'
    elif char.lower() == 'з':
        res = 'z'
    elif char.lower() == 'х':
        res = 'h'
    elif char.lower() == 'ъ':
        res = '#'
    elif char.lower() == 'ф':
        res = 'f'
    elif char.lower() == 'ы':
        res = 'y'
    elif char.lower() == 'в':
        res = 'v'
    elif char.lower() == 'а':
        res = 'a'
    elif char.lower() == 'п':
        res = 'p'
    elif char.lower() == 'р':
        res = 'r'
    elif char.lower() == 'о':
        res = 'o'
    elif char.lower() == 'л':
        res = 'l'
    elif char.lower() == 'д':
        res = 'd'
    elif char.lower() == 'ж':
        res = 'z'
        res2 = 'h'
    elif char.lower() == 'э':
        res = 'j'
        res2 = 'e'
    elif char.lower() == 'я':
        res = 'y'
        res2 = 'a'
    elif char.lower() == 'ч':
        res = 'c'
        res2 = 'h'
    elif char.lower() == 'с':
        res = 's'
    elif char.lower() == 'м':
        res = 'm'
    elif char.lower() == 'и':
        res = 'i'
    elif char.lower() == 'т':
        res = 't'
    elif char.lower() == 'ь':
        res = "'"
    elif char.lower() == 'б':
        res = 'b'
    elif char.lower() == 'ю':
        res = 'j'
        res2 = 'u'
    elif char.lower() == 'ё':
        res = 'j'
        res2 = 'o'

    if char != char.lower():
        return res.upper() + res2
    return res + res2


class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def change_price(self, price):
        if price[0] == '+':
            self.price += int(price[1:])
        elif price[0] == '-':
            self.price -= int(price[1:])
        elif price[0] == '*':
            self.price *= int(price[1:])
        elif price[0] == '/':
            self.price //= int(price[1:])
        else:
            self.price = int(price)

    def change_quantity(self, quantity):
        if quantity[0] == '+':
            self.quantity += int(quantity[1:])
        elif quantity[0] == '-':
            self.quantity -= int(quantity[1:])
        elif quantity[0] == '*':
            self.quantity *= int(quantity[1:])
        elif quantity[0] == '/':
            self.quantity //= int(quantity[1:])
        else:
            self.quantity = int(quantity)

    def __str__(self):
        return self.name + ':\tЦена - ' + str(self.price) + "р\tКол-во - " + str(self.quantity) + "шт."


task = 1
while task > 0:
    task = int(input("Введите номер задачи или 0 для выхода: "))

    if task == 1:
        arr_1 = np.ndarray((3, 4), dtype=int)
        arr_1.fill(3)
        print("arr_1 size:", arr_1.size)

        arr_2 = np.random.randint(0, 9, size=(2, 4))
        print("arr_2 size:", arr_2.size)

        print("arr_1 + arr_2:\n", np.concatenate((arr_1, arr_2), axis=0))

        arr_3 = np.array((1, 8, 6, 5, 8, 3))
        arr_3 *= 3
        arr_3 += 1

        arr_4 = arr_3.copy()

        arr_3 = arr_3.reshape((2, 3))
        arr_5 = arr_3.copy()

        print("arr_4:\n", arr_4, "\narr_5:\n", arr_5)
        print("arr_5 min: ", np.min(arr_5, axis=1), "\narr_5 average: ", np.average(arr_5))

        arr_6 = np.ndarray((11, 1), dtype=int)
        for i in range(11):
            arr_6.put(i, i ** 2)
        print("Каждый второй элемент arr_6:\n", arr_6[1::2])
        print("arr_6 в обратном порядке:\n", arr_6[::-1])

        for i in range(1, 11, 2):
            arr_6.put(i, 2)
        print(49 in arr_6)

        A = np.random.randint(-10, 10, size=(5, 5))
        print("A:\n", A)

        B = A[A < 0]
        print("B (Все элементы из A, которые < 0):\n", B)
    elif task == 2:
        myField = make_field(int(input("Введите размер поля: ")))
        print(myField)
    elif task == 3:
        A, B = super_sort(int(input("Введите число строк: ")), int(input("Введите число столбцов: ")))
        print("Массив случайных чисел:\n", A)
        print("Отсортированный по условиям задачи массив:\n", B)
    elif task == 4:
        bw_convert("tboi.jpg")
    elif task == 5:
        print("Не готово")
    elif task == 6:
        f = open("lines.txt", encoding="utf-8")
        strs = f.readlines()
        if strs:
            _str = strs[np.random.randint(0, len(strs))]
            if _str[-1] == '\n':
                print(_str[:-1])
            else:
                print(_str)
        f.close()
    elif task == 7:
        f = open("cyrillic.txt", encoding="utf-8")
        lines = f.readlines()
        f.close()

        linesres = []
        for line in lines:
            lineres = ''
            for char in line:
                lineres += cyrillic_to_latin(char)
            linesres.append(lineres)

        f = open("transliteration.txt", 'w', encoding="utf-8")
        f.writelines(linesres)
        f.close()
    elif task == 8:
        print("Не готово")
    elif task == 9:
        f = open("input.txt", encoding="utf-8")
        lines = f.readlines()
        f.close()

        counter = 0
        positive = 0
        negative = 0
        zero = 0
        numbers = []

        for line in lines:
            _str = ''
            if line[-1] != '\n':
                line += ' '

            for char in line:
                if char in ['+', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    _str += char
                elif _str:
                    numbers.append(_str)
                    _str = ''

        for i in numbers:
            num = int(i)
            if num > 0:
                positive += 1
            elif num < 0:
                negative += 1
            else:
                zero += 1

        f = open("output.txt", 'w', encoding="utf-8")
        f.write(str(len(numbers)) + '\n')
        if positive > 0:
            f.write('1 ' + str(positive) + ' ')
        if negative > 0:
            f.write('-1 ' + str(negative) + ' ')
        if zero > 0:
            f.write('0 ' + str(zero))
        f.close()
    elif task == 10:
        print("Не готово")
    elif task == 11:
        catalog = []
        while task > 0:
            task = int(input("1. Список товаров\n2. Добавить товар\n3. Изменить товар\n4. Загрузить из файла\n5. Сохранить в файл\n\n0. Выход:\t"))

            if task == 1:
                for i in catalog:
                    print(i)
            elif task == 2:
                catalog.append(Product(input("Имя товара: "), int(input("Цена товара: ")), int(input("Кол-во товара: "))))
            elif task == 3:
                counter = 1
                for i in catalog:
                    print(counter + '. ', i)
                counter = int(input("Введите номер товара: "))

                task = int(input("1. Название товара\n2. Цену товара\n3. Кол-во товара:\t"))

                if task == 1:
                    catalog[counter - 1].name = input("Новое имя: ")
                elif task == 2:
                    catalog[counter - 1].change_price(input("Изменение цены: "))
                elif task == 3:
                    catalog[counter - 1].change_quantity(input("Изменение кол-ва: "))
            elif task == 5:
                with open('Shop.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(["Board Game", "Price", "Quantity"])
                    for i in catalog:
                        writer.writerow([i.name, i.price, i.quantity])
            elif task == 4:
                catalog = []
                with open('Shop.csv') as csvfile:
                    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                    for index, row in enumerate(reader):
                        if index > 0:
                            catalog.append(Product(row[0], int(row[1]), int(row[2])))
