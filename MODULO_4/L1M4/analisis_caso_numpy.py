# MÓDULO 4 - Lección 1 - Análisis de Caso NumPy

import numpy as np

# Creación de datos financieros simulados

# Se fija para que siempre se generen los mismos números

np.random.seed(1)

# se crea una matriz 5x5:

precios = np.random.randint(100, 200, size=(5, 5))

print("Matriz de precios simulados:")
print(precios)


# Estadísticas básicas por acción

promedio = np.mean(precios, axis=1)
maximo = np.max(precios, axis=1)
minimo = np.min(precios, axis=1)

print("\nPromedio por acción:")
print(promedio)

print("\nMáximo por acción:")
print(maximo)

print("\nMínimo por acción:")
print(minimo)


# Variación porcentual diaria

# se compara cada día con el anterior

variacion = (precios[:, 1:] - precios[:, :-1]) / precios[:, :-1] * 100

print("\nVariación porcentual diaria:")
print(variacion)


# Transformaciones matemáticas

# Logaritmo natural de los precios

log_precios = np.log(precios)

print("\nLogaritmo de los precios:")
print(log_precios)


# Normalización de los datos

# Normalizar usando la media y desviación estándar global

media_global = np.mean(precios)
desviacion_global = np.std(precios)

normalizado = (precios - media_global) / desviacion_global

print("\nDatos normalizados:")
print(normalizado)


# Indexación específica

# Se extrae el precio de la acción 3 en el día 4

# (recordar que los índices empiezan en 0)

valor_especifico = precios[2, 3]

print("\nPrecio acción 3 día 4:", valor_especifico)


# Ejemplo de broadcasting

# Simulando un aumento del mercado del 2%

precios_ajustados = precios * 1.02

print("\nPrecios con aumento del 2%:")
print(precios_ajustados)
