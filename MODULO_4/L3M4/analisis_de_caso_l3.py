import pandas as pd

# =====================================
#       PASO 1: CARGA DE DATOS
# =====================================

# CSV
df_clientes = pd.read_csv("clientes_ecommerce.csv")

# Excel
df_ventas_2025 = pd.read_excel(
    "ventas_ecommerce_2025_2026.xlsx",
    sheet_name="ventas_2025"
)

df_ventas_2026 = pd.read_excel(
    "ventas_ecommerce_2025_2026.xlsx",
    sheet_name="ventas_2026"
)

# Tabla Web
url = "https://www.w3schools.com/html/html_tables.asp"
tablas = pd.read_html(url)
df_web = tablas[0]

print("Carga de datos completada")

# =====================================
#   PASO 2: LIMPIEZA Y ESTRUCTURACIÓN
#         (Se trabajará sobre el DataFrame de clientes)
# =====================================

print("\nValores nulos:")
print(df_clientes.isnull().sum())

print("\nTipos de datos:")
print(df_clientes.dtypes)

duplicados = df_clientes.duplicated().sum()
print(f"\nDuplicados encontrados: {duplicados}")

# Eliminación de duplicados si existen
df_clientes = df_clientes.drop_duplicates()

print("Duplicados después de limpieza:", df_clientes.duplicated().sum())

# Convertir fecha a datetime
df_clientes["fecha_registro"] = pd.to_datetime(df_clientes["fecha_registro"])

# Imputar edad con la mediana
df_clientes["edad"] = df_clientes["edad"].fillna(df_clientes["edad"].median())

# Imputar ingreso con mediana
df_clientes["ingreso_mensual"] = df_clientes["ingreso_mensual"].fillna(
    df_clientes["ingreso_mensual"].median()
)

# Imputar ingreso como "Sin Información"
df_clientes["region"] = df_clientes["region"].fillna("Sin información")

print("\nValores nulos después de limpieza:")
print(df_clientes.isnull().sum())

# =====================================
# PASO 3: TRANSFORMACIÓN Y OPTIMIZACIÓN
# =====================================

# Seleccionar columnas relevantes para análisis
df_clientes_limpio = df_clientes[
    ["cliente_id", "genero", "edad", "region", "ingreso_mensual", "activo"]
]

# Renombrar columnas para mejor legibilidad
df_clientes_limpio = df_clientes_limpio.rename(columns={
    "cliente_id": "id_cliente",
    "genero": "sexo",
    "edad": "edad_cliente",
    "region": "region_cliente",
    "ingreso_mensual": "ingreso",
    "activo": "cliente_activo"
})

# Ordenar por ingreso descendente
df_clientes_limpio = df_clientes_limpio.sort_values(
    by="ingreso",
    ascending=False
)

print("\nDataFrame transformado:")
print(df_clientes_limpio.head())

# =====================================
#     PASO 4: EXPORTACIÓN DE DATOS
# =====================================

# Guardar CSV limpio sin índice
df_clientes_limpio.to_csv(
    "clientes_limpios_procesados.csv",
    index=False
)

# Exportar a Excel
df_clientes_limpio.to_excel(
    "clientes_limpios_procesados.xlsx",
    index=False
)

print("\nArchivos exportados correctamente.")