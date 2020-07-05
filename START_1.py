
from classes import Vector ## импорт необходимых модулей
from functions import *

Va = Vector()                            ## создаём экземпляры класса Vector
Vb = Vector()

i=1                                         ## устанавливаем флаг
    
while i==1:                               ## выход из цикла при удачном вводе данных
    try:  
        Va.X = float(input("\n Xa = "))     ## ввод координаты Х вектора 'а'
        i+=1                                ## увеличиваем значение на 1 для выхода из цикла                  
    except Exception as err:                ## обработка некорректного ввода данных
        WriteLogError2(err)                 ## импортируемая функция записи ошибок в журнал
while i==2:                               ## далее еще 5 аналогичных блоков try except для ввода координат
    try:
        Vb.X = float(input("\t\t\t\t Xb = "))
        i+=1
    except Exception as err:
        WriteLogError2(err)

while i==3:  
    try:
        Va.Y = float(input("\n Ya = "))
        i+=1
    except Exception as err:
        WriteLogError2(err)

while i==4:
    try:
        Vb.Y = float(input("\t\t\t\t Yb = "))
        i+=1
    except Exception as err:
        WriteLogError2(err)

while i==5:
    try:            
        Va.Z = float(input("\n Za = "))
        i+=1
    except Exception as err:
        WriteLogError2(err)
        
while i==6:
    try:
        Vb.Z = float(input("\t\t\t\t Zb = "))
        i+=1
    except Exception as err:
        WriteLogError2(err)

pictures()

print("УГОЛ МЕЖДУ ВЕКТОРАМИ = ", Angle(Va,Vb), chr(176))

Va.coordinates() ## вывод на экран координат векторов
Vb.coordinates()

print("\n")
print("=====================================")
input("для завершения нажмите Enter")
## чтобы не закрывалось окно консоли при завершении программы
