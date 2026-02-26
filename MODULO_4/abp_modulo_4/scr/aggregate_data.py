import pandas as pd


# ======================================================
# AGRUPACIONES PRINCIPALES
# ======================================================

def ventas_por_categoria(df):
    resumen = (
        df.groupby("nombre_categoria")["total_venta"]
        .sum()
        .reset_index()
        .sort_values(by="total_venta", ascending=False)
    )
    return resumen


def ventas_por_canal(df):
    resumen = (
        df.groupby("canal_venta")["total_venta"]
        .sum()
        .reset_index()
        .sort_values(by="total_venta", ascending=False)
    )
    return resumen


def ventas_por_mes(df):
    resumen = (
        df.groupby(["año", "mes"])["total_venta"]
        .sum()
        .reset_index()
        .sort_values(by=["año", "mes"])
    )
    return resumen


# ======================================================
# PIVOT TABLE
# ======================================================

def pivot_categoria_canal(df):
    tabla = pd.pivot_table(
        df,
        values="total_venta",
        index="nombre_categoria",
        columns="canal_venta",
        aggfunc="sum",
        fill_value=0
    )
    return tabla

# ======================================================
# MELT DE PIVOT (FORMATO LARGO)
# ======================================================

def melt_categoria_canal(tabla_pivot):
    df_melt = tabla_pivot.reset_index().melt(
        id_vars="nombre_categoria",
        var_name="canal_venta",
        value_name="total_venta"
    )
    return df_melt