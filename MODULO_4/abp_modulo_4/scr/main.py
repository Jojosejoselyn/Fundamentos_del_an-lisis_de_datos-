import os
from load_data import load_datasets
from clean_data import clean_clientes, clean_productos, clean_categorias, clean_ventas
from transform_data import build_sales_master


def main():

    data = load_datasets()

    data["clientes"] = clean_clientes(data["clientes"])
    data["productos"] = clean_productos(data["productos"])
    data["categorias"] = clean_categorias(data["categorias"])
    data["ventas"] = clean_ventas(data["ventas"])

    master_df = build_sales_master(data)

    print("\n==============================")
    print("DATASET MASTER LIMPIO")
    print("==============================")
    print(master_df.head())

    # EXPORTACIÓN (dentro de main)
    master_df.to_csv("../data/processed/dataset_final.csv", index=False)
    master_df.to_excel("../data/processed/dataset_final.xlsx", index=False)


if __name__ == "__main__":
    main()