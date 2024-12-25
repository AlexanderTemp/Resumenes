# Python

## 1. Asignación multiple de variables

Con una coma se puede asignar multiples variables o hacer cambio en dos variables

```python
a = 10
b = 20
a, b = 30, 40
print(a, b)
a, b = b, a
print(a, b)
```

## 2. Variable Local vs Global

Si se quiere modificar una variabla global dentro una función se usa global para referenciar a la var. global.

```python
var1 = 20
def abc():
  global var1
  var1 = 50

print(var1)
abc()
print(var1)
```

## 3. Assert

Para pruebas se verificar si la variable tiene cierto valor.

```python
a = 10
assert a == 10 ## True, el código sigue sin problemas
assert a == 20 ## False, se levanta un error AssertionError
```

## 4. String multiple

Cuando se quiere imprimir de cierta manera específica con salto de líneas y demás.

```python
str = """
Dos
y dos son cuatro4
son                       6
"""
print(str) ## Se imprime igual
```

## 5. Impresiones con string

```python
d = "this's python"
print("this is output %s", %d)
name = "python"
print(len(name))
```

## 6. Tipo de dato

```python
type("hola mundo")
```

## 7. Precedencia de operadores

\*_, _, /, //, %, `, - (siempre usar parentesis)

## 8. Operaciones con string

Se concatena con + y se replica con \*.

```python
a = 'A' + 'B'
print(a)
b = 'A'* 5
print(b)
```

## 9. Conversores

str(), int(), float()

## 10. Operadores de comparación

==, :=, <, >, <=, >=

## 11. Estructura for

range(inicio, < final, salto)

```python
# impresión de números del 1 al 10
for i in range(1, 11, 1):
  print(i, " ", end="")
```

## 12. Módulo sys

Acceso a variables del interprete python

```python
import sys

print(sys.argv) # Lista de argumentos pasados al script
sys.exit()  # Termina la ejecución del programa
print(sys.version)  # Versión de Python
print(sys.platform)  # Plataforma en la que se ejecuta (e.g., 'win32', 'linux')
sys.stdout.write("Hola\n")  # Imprimir sin usar `print`
sys.setrecursionlimit(2000)  # Cambia el límite de recursión
```

## 13. None y null

A diferencia de otros lenguajes None es igual a null en python < NoneType >, representa la ausencia de valor o valor nulo.

## 14. Keyword arguments

Controlan el comportamiento de la función print.

```python
print("Hola", "mundo", sep="-")  # Salida: Hola-mundo

print("Hola", end=", ")
print("mundo")  # Salida: Hola, mundo

# file destino de salida
with open("salida.txt", "w") as f:
    print("Esto va al archivo", file=f)

# flush vaciado de bufer, útil en impresion en tiempo real
import time
for i in range(3):
    print(i, end=" ", flush=True)
    time.sleep(1)  # Salida inmediata: 0 1 2

# Ejemplo
print("Python", "es", "genial", sep="💡", end="!\n", flush=True)
# Salida: Python💡es💡genial!
```

## 15. Uso de slices
