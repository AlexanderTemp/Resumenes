class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre=nombre
        self.edad=edad
        self.nota=nota
    def obtenerNota(self):
        return self.nota

class Curso:
    def __init__(self, nombreCurso, maximoEstudiantes):
        self.nombreCurso=nombreCurso
        self.maximoEstudiantes=maximoEstudiantes
        self.estudiantes=[]
    
    def nuevo_estudiante(self, estudiante):
        if len(self.estudiantes)<self.maximoEstudiantes:
            self.estudiantes.append(estudiante)
            return True
        else: 
            return False
    def obtenerPromedioNotas(self):
        sum=0
        for estudiante in self.estudiantes:
            sum+=estudiante.obtenerNota
        return sum
    
class main:
    s1=Estudiante("Jaime", 18, 98)
    s2=Estudiante("Pepe", 17, 60)
    s3=Estudiante("Pablo", 20, 40)
    curso=Curso("Matemáticas", 2)
   
    if curso.nuevo_estudiante(s1):
        print(f"Estudiante {s1.nombre} añadido exitosamente")
    else:
        print("Cupo lleno")
        
    