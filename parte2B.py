cuadrante1=0 # x,y son positivos
cuadrante2=0 # x negativo, y positivo
cuadrante3=0 #x, y son negativos
cuadrante4=0 # x es positivo, y es negativo
n=int(input("Cantidad de puntos:")) 
for f in range(n): 
    x=int(input("Ingrese coordenada x:")) 
    y=int(input("Ingrese coordenada y:"))
# continuar con el condicional
    if x > 0 and y >0:
        cuadrante1+=1
    elif x <0  and y >0:
        cuadrante2+=1
    elif x <0  and y <0:
        cuadrante3+=1
    else: 
       cuadrante4+=1
    # imprimir
    print("Puntos en el cuadrante 1:", cuadrante1) 
    print("Puntos en el cuadrante 2:", cuadrante2)
    print("Puntos en el cuadrante 3:", cuadrante3) 
    print("Puntos en el cuadrante 4:", cuadrante4)
