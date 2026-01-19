contador = 1

while contador <= 5:
    print(f"Numero: {contador}")
    contador = contador + 1

print("Fin del loop!")

print("--------------")

#-----------------------------------------------------
contador = 5

while contador >= 1:
    print(f"Numero: {contador}")
    contador = contador - 1

print("Fin del loop!")

#-----------------------------------------------------
print("--------------")

contador = 1
while contador <= 20:
    if contador == 15:
        break
    if contador % 3 == 0:
        contador += 1
        continue
    print(contador)
    contador += 1
    

print("Fin del loop!")

#-----------------------------------------------------
print("--------------")

contador = 1
while contador <= 20:
    print(f"{contador} / 3 es: {contador % 3}")
    contador += 1
    
    

