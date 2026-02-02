
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")
    print("---------------------")
    if operacion == "+":
        print("Resultado:", num1 + num2)

    elif operacion == "-":
        print("Resultado:", num1 - num2)

    elif operacion == "*":
        print("Resultado:", num1 * num2)

    elif operacion == "/":
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        print("Resultado:", num1 / num2)

    else:
        print("Error: /n")
        print("Operación no válida")
    
    print("---------------------")

except Exception as e:
    print("---------------------")
    # print("Error debe ingresar un número valido y operación valida:", e)
    print("Error debe ingresar un número valido y operación valida:")
    print("---------------------")
