class Persona:
    def __init__(self, primerNombre, primerApellido):
        self.primerNombre=primerNombre
        self.primerApellido=primerApellido
    def mostrarNombre(self):
        print(f'{self.primerNombre} {self.primerApellido}')

persona1=Persona("Jaime", "Perez")
persona1.mostrarNombre()

print("################################")

class Estudiante(Persona):
    def __init__(self, primerNombre, primerApellido, anio):
        super().__init__(primerNombre, primerApellido)
        self.anioIngreso=anio
    
    def bienvenido(self):
        print(f"Bienvenido {self.primerNombre}, {self.primerApellido} del año {self.anioIngreso}")
        
estudiante1=Estudiante("Federico", "Buendia", 2020)
estudiante1.bienvenido()
estudiante1.mostrarNombre()