import os
import pandas as pd


def load_datasets():
    """
    Carga todos los datasets desde data/raw.
    Retorna un diccionario con los DataFrames.
    """

    # Ruta base del proyecto (sube desde src hasta abp_modulo_4)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    print("BASE_DIR:", BASE_DIR)  # <-- Esto es para verificar

    clientes_path = os.path.join(BASE_DIR, "data", "raw", "clientes_ecommerce.csv")
    productos_path = os.path.join(BASE_DIR, "data", "raw", "productos.csv")
    categorias_path = os.path.join(BASE_DIR, "data", "raw", "categorias.csv")
    ventas_path = os.path.join(BASE_DIR, "data", "raw", "ventas_ecommerce_2025_2026.xlsx")

    print("Ruta clientes:", clientes_path)  # <-- Verificación

    clientes = pd.read_csv(clientes_path)
    productos = pd.read_csv(productos_path)
    categorias = pd.read_csv(categorias_path)
    ventas = pd.read_excel(ventas_path)

    return {
        "clientes": clientes,
        "productos": productos,
        "categorias": categorias,
        "ventas": ventas
    }


def inspect_datasets(data_dict):
    for name, df in data_dict.items():
        print(f"\n{'='*50}")
        print(f"DATASET: {name.upper()}")
        print(f"{'='*50}")
        print("Dimensiones:", df.shape)
        print("Primeras filas:")
        print(df.head())