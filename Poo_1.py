class Punto:
    def __init__(self, x, y):
        self.__x=x
        self.__y=y
    ## Getters
    def obtenerX(self):
        return self.__x
    def obtenerY(self):
        return self.__y
    ## Setters
    def modificarX(self, x):
        self.__x=x
    def modificarY(self, y):
        self.__y=y
        
    def mostrarCoordenadas(self):
        print(f'(x={self.__x}, y={self.__y})')
        
punto1=Punto(2, 3)
punto2=Punto(4, 5)
punto3=Punto(9, -1)
punto1.mostrarCoordenadas()
punto2.mostrarCoordenadas()
punto3.mostrarCoordenadas()

print("punto3")
punto3.modificarX(100)
punto3.mostrarCoordenadas()
