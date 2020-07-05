import math

class Vector:
    
    def __init__(self, X=None, Y=None, Z=None): # конструктор
        
        self.X = X  # устанавливаем координаты вектора
        self.Y = Y
        self.Z = Z
        
    def coordinates(self): # метод печатает координаты вектора
        print("вектор = {", self.X,";", self.Y,";", self.Z,"}" )

    def vector_length(self): # возвращает длину вектора
        return float(math.sqrt(math.pow(self.X, 2) + math.pow(self.Y, 2) + math.pow(self.Z, 2)))
