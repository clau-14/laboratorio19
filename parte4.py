estudiantes = { 

}
n= int( input("cuantos estudiantes vas a procesar"))
x=1
while x<=n:
    nombre= input("nombre delo estudiante")
    calificacion=float(input("calificacion: "))
    estudiantes [nombre]= calificacion
    for clave , valor in estudiantes.items():
        print(f"{clave}: {valor}") #imprime cada par clave y valor