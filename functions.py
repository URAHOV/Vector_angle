
def WriteLogError2(err): ##функция записи ошибок в log_err.txt
    import datetime  
    err = str(err)
    time1 = datetime.datetime.today().strftime('%Y-%m-%d_%H.%M.%S')

    with open("log_err2.txt", "a") as log_err:
        log_err.write("\n"+time1+" - "+err)
        
    print(" \n!!!--- Нужно ввести целое или дробное число ---!!!")
    print("!!!  (дробное число вводится через точку 5.56) !!!")

def Angle(Va,Vb): ## функция возвращает значение угла между векторами
    import math
    return float(round(math.degrees(math.acos(\
        (Va.X*Vb.X + Va.Y*Vb.Y + Va.Z*Vb.Z)/\
        (Va.vector_length() * Vb.vector_length()))), 2))
    

def pictures(): ## функция печатает рисунок угла ;-)
    print("\t\\\t\t\t /")
    print("\t \\\t\t        /")
    print("\t  \\\t\t       /")
    print("\t   \\\t\t      /")
    print("\t    \\\t\t     /")
    print("\t     \\\t\t    /")
    print("\t      \\\t\t   /")
    print("\t       \\\t  /")
    print("\t        \\\t /")
    print("\t         \\      /")
    print("\t          \\    /")
    print("\t           \\  /")
    print("\t            \\/")
