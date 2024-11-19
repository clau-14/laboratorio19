estudiantes = { 
"Juan": 2.0, 
"Ana": 4.2, 
"Luis": 4.5 
}
estudiante=""
nota_mayor= 0

for clave, valor in estudiantes.items():
   print(f"{clave}: {valor}")

   if valor> nota_mayor:
        estudiantes=clave
        nota_mayor=valor
        print(f"el estudiante con la calificacion mas alta es {estudiantes} con una calificacion de {nota_mayor}")
