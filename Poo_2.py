class Fecha:
    def __init__(self, dia, mes):
        self.__dia=dia
        self.__mes=mes
    ## Getters
    def obtenerDia(self):
        return self.__dia
    def obtenerMes(self):
        return self.__mes
    ## Metodos
    def igual(self, fecha):
        if fecha.obtenerDia()==self.__dia and fecha.obtenerMes()==self.__mes:
            return True
        else:
            return False
    def visualizar(self):
        print(f'mes={self.__mes}, dia={self.__dia}')
    

hoy=Fecha(1, "Julio")
cumple=Fecha(30, "Mayo")
print("La fecha de hoy es: ")
hoy.visualizar()
print("Tu fecha de nacimiento es: ")
cumple.visualizar()
if hoy.igual(cumple):
    print("Feliz Cumpleaños 😊")
else:
    print("Todavía falta para tu cumpleaños😔")


a=34
print(type(a))
hoy=Fecha(1, "Julio")
print(type(hoy))

    
    