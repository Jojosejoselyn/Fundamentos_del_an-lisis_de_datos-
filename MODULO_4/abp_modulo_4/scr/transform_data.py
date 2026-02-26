import pandas as pd


# ======================================================
# BUILD DATASET MASTER
# ======================================================

def build_sales_master(data):

    ventas = data["ventas"]
    clientes = data["clientes"]
    productos = data["productos"]
    categorias = data["categorias"]

    print("Filas originales ventas:", len(ventas))

    # Merge clientes
    df = ventas.merge(
        clientes,
        on="cliente_id",
        how="left"
    )
    print("Después merge clientes:", len(df))

    # Merge productos
    df = df.merge(
        productos,
        on="producto_id",
        how="left"
    )
    print("Después merge productos:", len(df))

    # Merge categorias
    df = df.merge(
        categorias,
        on="categoria_id",
        how="left"
    )
    print("Después merge categorias:", len(df))

    # ======================================================
    # DATA WRANGLING PROFESIONAL
    # ======================================================

    # 1️⃣ Crear año y mes
    df["año"] = df["fecha_venta"].dt.year
    df["mes"] = df["fecha_venta"].dt.month

    # 2️⃣ Ticket promedio por venta
    df["ticket_promedio"] = df["total_venta"] / df["cantidad"]

    # 3️⃣ Clasificación de ingreso cliente
    df["segmento_ingreso"] = pd.cut(
        df["ingreso_mensual"],
        bins=[0, 800000, 1500000, 999999999],
        labels=["Bajo", "Medio", "Alto"]
    )

    # 4️⃣ Clasificación de edad con lambda
    df["rango_edad"] = df["edad"].apply(
        lambda x: "Joven" if x < 30 else
                  "Adulto" if x < 60 else
                  "Senior"
    )

    # 5️⃣ Normalizar total_venta (escala 0–1)
    df["total_normalizado"] = (
        (df["total_venta"] - df["total_venta"].min()) /
        (df["total_venta"].max() - df["total_venta"].min())
    )

    return df