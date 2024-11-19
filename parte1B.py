numero =int(input("Escribe un numero positivo"))

if 1 <= numero <= 999:
    if numero < 10:
        print("El número tiene un dígito.")
    elif numero < 100:
        print("El número tiene dos dígitos.")
    else:
        print("El número tiene tres dígitos.")
else:
    print("El número ingresado no está en el rango permitido (1..999).")
