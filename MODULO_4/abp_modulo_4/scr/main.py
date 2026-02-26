import os
import pandas as pd

from load_data import load_datasets

from clean_data import (
    clean_clientes,
    clean_productos,
    clean_categorias,
    clean_ventas
)

from transform_data import build_sales_master

from aggregate_data import (
    ventas_por_categoria,
    ventas_por_canal,
    ventas_por_mes,
    pivot_categoria_canal,
    melt_categoria_canal
)


def main():

    # ======================================================
    # BASE PATH
    # ======================================================

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("BASE_DIR:", BASE_DIR)

    # ======================================================
    # CARGA DE DATOS
    # ======================================================

    data = load_datasets()

    # ======================================================
    # LIMPIEZA
    # ======================================================

    data["clientes"] = clean_clientes(data["clientes"])
    data["productos"] = clean_productos(data["productos"])
    data["categorias"] = clean_categorias(data["categorias"])
    data["ventas"] = clean_ventas(data["ventas"])

    # ======================================================
    # TRANSFORMACIÓN (MERGES + FEATURES)
    # ======================================================

    master_df = build_sales_master(data)

    print("\n==============================")
    print("DATASET MASTER LIMPIO")
    print("==============================")
    print(master_df.head())

    # ======================================================
    # AGRUPACIONES
    # ======================================================

    print("\n==============================")
    print("AGRUPACIONES")
    print("==============================")

    resumen_categoria = ventas_por_categoria(master_df)
    resumen_canal = ventas_por_canal(master_df)
    resumen_mes = ventas_por_mes(master_df)
    tabla_pivot = pivot_categoria_canal(master_df)
    tabla_melt = melt_categoria_canal(tabla_pivot)

    print("\nVentas por categoría:")
    print(resumen_categoria)

    print("\nVentas por canal:")
    print(resumen_canal)

    print("\nVentas por mes:")
    print(resumen_mes)

    print("\nPivot categoría vs canal:")
    print(tabla_pivot)

    print("\nTabla en formato largo (melt):")
    print(tabla_melt)

    # ======================================================
    # EXPORTACIÓN
    # ======================================================

    processed_path = os.path.join(BASE_DIR, "data", "processed")
    os.makedirs(processed_path, exist_ok=True)

    master_df.to_csv(os.path.join(processed_path, "dataset_final.csv"), index=False)

    with pd.ExcelWriter(os.path.join(processed_path, "reporte_final.xlsx")) as writer:
        master_df.to_excel(writer, sheet_name="Dataset_Master", index=False)
        resumen_categoria.to_excel(writer, sheet_name="Ventas_por_Categoria", index=False)
        resumen_canal.to_excel(writer, sheet_name="Ventas_por_Canal", index=False)
        resumen_mes.to_excel(writer, sheet_name="Ventas_por_Mes", index=False)
        tabla_pivot.to_excel(writer, sheet_name="Pivot_Categoria_Canal")
        tabla_melt.to_excel(writer, sheet_name="Melt_Categoria_Canal", index=False)

    print("\n✔ Archivos exportados correctamente en data/processed/")


if __name__ == "__main__":
    main()