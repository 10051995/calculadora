def sumar(a, b): 
    return a + b 

def restar(a, b): 
    return a - b 

def multiplicar(a, b): 
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b 

# Menú de operaciones
print("Calculadora básica") 
print("1. Sumar")
print("2. Restar")  
print("3. Multiplicar")
print("4. Dividir")  

opcion = input("Selecciona una opción (1/2/3/4): ")

# Solicitar números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == '1':
    resultado = sumar(num1, num2)
    print(f"El resultado de la suma es: {resultado}")
elif opcion == '2': 
    resultado = restar(num1, num2)
    print(f"El resultado de la resta es: {resultado}") 
elif opcion == '3':
    resultado = multiplicar(num1, num2)
    print(f"El resultado de la multiplicación es: {resultado}") 
elif opcion == '4':
    resultado = dividir(num1, num2)
    print(f"El resultado de la división es: {resultado}")  
else:
    print("Opción inválida")
