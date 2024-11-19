n=int(input("Cuantos empleados tiene la empresa:")) 

conta1=0 #total empleado entre 1 y 3 millones
conta2=0 #total empleado  3 millones
x=1 
while x <=n:
     
    salario= float(input(f"sueldo del empleado {x}: "))
    if salario <1000000 or salario>5000000:
        print("salario no valido")
        continue
    if salario >3000000:
        conta2= conta2 +1
    else: 
        conta1= conta1 +1
    x=x+1     

print(f"empleados que ganan mas de 3 millones: {conta2}")
print(f"empleados que ganan entre 1 y  3 millones: {conta1}")