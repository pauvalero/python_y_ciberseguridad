# EJERCICIO COMPLETO: DOMINANDO LOS OPERADORES EN PYTHON
# Completa los espacios, responde las preguntas y corrige los errores

# ========== PARTE 1: OPERADORES ARITMÉTICOS ==========
print("=== PARTE 1: Operadores Aritméticos ===")

# Completa las operaciones que faltan
num1 = 20
num2 = 6

resultado_suma = num1 + num2          # Debe dar 26
resultado_resta = num1 - num2         # Debe dar 14
resultado_mult = num1 * num2          # Debe dar 120
resultado_div = num1 / num2           # Debe dar 3.33...
resultado_div_entera = num1 // num2    # Debe dar 3
resultado_modulo = num1 % num2        # Debe dar 2
resultado_potencia = num1 ** num2      # Debe dar 64,000,000?

# Corrige el error en esta expresión
# resultado = 10 + 5 * 2  # Resultado esperado: 20, actual: ¿?
resultado_corregido = 10 + 5 * 2
# ¿Cómo lo corregirías para que dé 30? ________________
resultado_corregido = (10 + 5) * 2

# ========== PARTE 2: OPERADORES DE COMPARACIÓN ==========
print("\n=== PARTE 2: Operadores de Comparación ===")

a = 15
b = 10
c = 15

# Escribe el resultado esperado (True/False)
comp1 = a > b          # Esperado: True
comp2 = a == c         # Esperado: True  
comp3 = b != a         # Esperado: True
comp4 = a <= c         # Esperado: True
comp5 = 20 >= a        # Esperado: True

# Explica qué hace esta expresión combinada
edad = 25
altura = 175
expresion_compleja = (edad >= 18) and (altura > 160)
# Explicación: Primero verifica si la edad es mayor o igual a 18, y despues verifica si la altura es mayor a 160. El resultado es True

# ========== PARTE 3: OPERADORES LÓGICOS ==========
print("\n=== PARTE 3: Operadores Lógicos ===")

# Completa con and, or, not
es_fin_de_semana = True
tengo_dinero = False
hace_buen_tiempo = True

puedo_salir = es_fin_de_semana and (tengo_dinero or hace_buen_tiempo)
# ¿Cuándo puedo salir? Puedo salir cuando sea fin de semana y tenga dinero o haga buen tiempo

es_adulto = True
es_estudiante = False
tiene_descuento = not es_estudiante or (edad > 65)
# ¿Quién tiene descuento? Los estudiantes y los mayores de 65 años

# ========== PARTE 4: OPERADORES DE ASIGNACIÓN ==========
print("\n=== PARTE 4: Operadores de Asignación ===")

# Cadena de operaciones complejas
x = 10
y = 5
z = 2

x += y * z            # x = 10 + 5 * 2 = 20
# ¿Cuál es el valor final de x? 20

# ========== PARTE 5: EXPRESIONES COMPLEJAS ==========
print("\n=== PARTE 5: Expresiones Complejas ===")

# Analiza y resuelve estas expresiones complejas
precio = 100
descuento = 20
iva = 21
es_cliente_frecuente = True
tiene_cupon = False

# Expresión 1: Calcula el precio final con descuento e IVA
precio_final = (precio - descuento) * (1 + iva/100)
# Explica paso a paso: El precio final se calcula restando el descuento al precio original y luego multiplicando el iva

# Expresión 2: Condición compleja para descuento extra
descuento_extra = es_cliente_frecuente and (tiene_cupon and (precio > 50))
# ¿Cuándo hay descuento extra? Si el cliente es frecuente, tiene un cupon y el precio es superior a 50

# Expresión 3: Múltiples condiciones
puede_comprar = (precio_final <= 150) or (tiene_cupon and es_cliente_frecuente)
# ¿Quién puede comprar? Si el precio final es inferior o igual a 150, o si tiene cupon y es cliente frecuente

# ========== PARTE 6: CORRECCIÓN DE ERRORES ==========
print("\n=== PARTE 6: Corrección de Errores ===")

# Corrige los errores en estas expresiones:
# 1. resultado = 10 + * 5           # Error: No se puede sumar y mutliplicar a la vez
#    Corrección: resultado = 10 + 5 o 10 * 5

# 2. if edad = 18:                  # Error: Asignacion en lugar de comparacion
#    Corrección: if edad == 18

# 3. valor = "10" + 5               # Error: No se pueden sumar str y int
#    Corrección: valor = int("10") + 5

# 4. if a > b and or c:             # Error: Sintaxis incorrecta en condicion logica
#    Corrección: if a > b and c

print("\n¡Ejercicio completado! Revisa todas tus respuestas.")