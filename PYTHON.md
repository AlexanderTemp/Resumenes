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

## 7. Comparar objetos

Cuando se compara un objeto no anidado se usa **is** y no ==

```python
obj = {
  hola: "mundo"
}

obj2 = {
  hola: "mundo"
}

print(obj == obj2)
print(obj is obj2)

```
