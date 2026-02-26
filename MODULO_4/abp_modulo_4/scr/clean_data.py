import pandas as pd
import numpy as np

# ======================================================
# LIMPIEZA CLIENTES
# ======================================================

def clean_clientes(df):
    df = df.copy()

    # Eliminar duplicados
    df = df.drop_duplicates(subset="cliente_id")

    # Manejo de valores nulos
    df["edad"] = df["edad"].fillna(df["edad"].median())
    df["ingreso_mensual"] = df["ingreso_mensual"].fillna(df["ingreso_mensual"].median())

    # Estandarizar texto
    df["nombre"] = df["nombre"].str.strip().str.title()
    df["apellido"] = df["apellido"].str.strip().str.title()
    df["email"] = df["email"].str.strip().str.lower()
    df["genero"] = df["genero"].str.strip().str.title()
    df["region"] = df["region"].str.strip().str.title()

    # Convertir tipos
    df["edad"] = df["edad"].astype(int)
    df["activo"] = df["activo"].astype(bool)

    return df


# ======================================================
# LIMPIEZA PRODUCTOS
# ======================================================

def clean_productos(df):
    df = df.copy()

    df = df.drop_duplicates(subset="producto_id")
    df["nombre_producto"] = df["nombre_producto"].str.strip().str.title()

    return df


# ======================================================
# LIMPIEZA CATEGORIAS
# ======================================================

def clean_categorias(df):
    df = df.copy()

    df = df.drop_duplicates(subset="categoria_id")
    df["nombre_categoria"] = df["nombre_categoria"].str.strip().str.title()

    return df


# ======================================================
# DETECCIÓN Y ELIMINACIÓN DE OUTLIERS (IQR)
# ======================================================

def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[column] >= lower) & (df[column] <= upper)]
    return df


# ======================================================
# LIMPIEZA VENTAS
# ======================================================

def clean_ventas(df):
    df = df.copy()

    # Eliminar duplicados
    df = df.drop_duplicates(subset="venta_id")

    # Convertir fecha
    df["fecha_venta"] = pd.to_datetime(df["fecha_venta"], errors="coerce")

    # Manejo de nulos numéricos
    df["cantidad"] = df["cantidad"].fillna(1)
    df["precio_unitario"] = df["precio_unitario"].fillna(df["precio_unitario"].median())

    # Recalcular total si fuera necesario
    df["total_venta"] = df["cantidad"] * df["precio_unitario"]

    # Eliminar outliers en total_venta
    df = remove_outliers_iqr(df, "total_venta")

    return df