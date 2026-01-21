historial = ""
while True:
     
        print("\n-- MENÚ ---")
        print("1 Sumar")
        print("2 Restar")
        print("3 Multiplicar")
        print("4 Dividir")
        print("5 Ver Historial")
        print("6 Salir")

        opcion = input("Elige una opción (1-6): ")

        #Suma
        if opcion == "1":
            try:
                cantidad = int(input("Cuántos números deseas sumar?: "))
                suma_total = 0
                
                for i in range(cantidad):
                    num = float(input(f"Ingresa el número {i+1}: "))
                    suma_total += num
                
                print(f"Resultado de la suma: {suma_total}")
                historial += f"Suma de {cantidad} números = {suma_total}\n"
            except ValueError:
                print("Error: Por favor ingresa números válidos.")

        #Restar
        elif opcion == "2":
            try:
                n1 = float(input("Ingresa el primer número: "))
                n2 = float(input("Ingresa el segundo número: "))
                res = n1 - n2
                print(f"Resultado: {res}")
                historial += f"Resta: {n1} - {n2} = {res}\n"
            except ValueError:
                print("Error: Dato no válido.")

        #Multiplicar
        elif opcion == "3":
            try:
                n1 = float(input("Ingresa el primer número: "))
                n2 = float(input("Ingresa el segundo número: "))
                res = n1 * n2
                print(f"Resultado: {res}")
                historial += f"Multiplicación: {n1} * {n2} = {res}\n"
            except ValueError:
                print("Error: Dato no válido.")

        #Dividir
        elif opcion == "4":
            try:
                n1 = float(input("Ingresa el dividendo: "))
                n2 = float(input("Ingresa el divisor: "))
                
                if n2 == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    res = n1 / n2
                    print(f"Resultado: {res}")
                    historial += f"División: {n1} / {n2} = {res}\n"
            except ValueError:
                print("Error: Dato no incorrecto.")

        #Historial
        elif opcion == "5":
            print("\n--- HISTORIAL ---")
            if historial == "":
                print("Aún no hay operaciones guardadas.")
            else:
                print(historial)

        #Salir
        elif opcion == "6":
            print("Cerrando")
            break

        else:
            print("Opción incorrecta")
