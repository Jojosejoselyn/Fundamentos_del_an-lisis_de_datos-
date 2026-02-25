from load_data import load_datasets, inspect_datasets

def main():
    data = load_datasets()
    inspect_datasets(data)

if __name__ == "__main__":
    main()