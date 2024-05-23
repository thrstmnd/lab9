import csv
import os
from PIL import Image, ImageFilter

def zadacha1():
    os.mkdir('image')
    for i in os.listdir('lab9\image'):
        jpg = Image.open(i)
        jpg = jpg.filter(ImageFilter.SMOOTH_MORE)
        jpg.save("C:\Users\user\PycharmProjects\lab9\image" + i + ".jpg")

def zadacha2():
    os.mkdir('image')
    for i in os.listdir('lab9\image'):
        if i.endswith('.jpg') or i.endswith('.png'):
            jpg = Image.open(i)
            jpg = jpg.filter(ImageFilter.SMOOTH_MORE)
            jpg.save("C:\Users\user\PycharmProjects\lab9\image" + i + ".jpg")

def zadacha3():
    summa=0
    print('Нужно купить:')
    with open('pokupki.csv') as file:
        file = csv.reader(file)
        for i in file:
            product=i[0]
            kolvo=int(i[1])
            cena=int(i[2])
            summa=summa+kolvo*cena
            print(product + " - " + kolvo + " шт. за " + cena + "руб.")
        print("Итоговая сумма: " + summa + "руб.")
