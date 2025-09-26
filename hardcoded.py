# PROGRAMA DE GESTIÓN DE ESTUDIANTES (CÓDIGO CON VALORES HARDCODEADOS)

nombre_estudiante = "María González" #string
curso = "Programación Python" #string
nota_1 = 8.5 #float
nota_2 = 7 #int
nota_3 = 9.2 #float
situacion_1 = "APROBADO ✓" #string
situacion_2 = "REPROBADO ✗" #string

print("=== SISTEMA DE NOTAS ===")
print(nombre_estudiante)
print(curso)
print(nota_1)
print(nota_2)
print(nota_3)

promedio = (8.5 + 7.0 + 9.2) / 3 #float
print(f"Promedio: {promedio:.2f}")

if promedio >= 7.0:
    print(situacion_1)
else:
    print(situacion_2)

print("Año académico: 2024")



