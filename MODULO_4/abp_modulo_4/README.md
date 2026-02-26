# Proyecto ABP - Módulo 4  
## Fundamentos del Análisis de Datos

### Descripción del Proyecto

El presente proyecto tiene como objetivo realizar un análisis exploratorio de un dataset de ventas e-commerce, aplicando técnicas de limpieza, transformación, agregación y visualización de datos.

Se desarrolló una estructura modular en Python para separar las etapas del proceso:

- `load_data.py` → Carga de datos  
- `clean_data.py` → Limpieza y validación  
- `transform_data.py` → Transformaciones  
- `aggregate_data.py` → Agregaciones  
- `main.py` → Ejecución del pipeline completo  

El análisis explicativo se documenta en el notebook:

- `analisis_explicativo.ipynb`

---

### Objetivos del Análisis

- Comprender la estructura del dataset.
- Analizar la tendencia temporal de ventas.
- Evaluar la distribución por categoría y canal.
- Estudiar el comportamiento del ticket promedio.
- Generar conclusiones estratégicas.

---

### Herramientas Utilizadas

- Python 3.x
- Pandas
- Matplotlib
- Jupyter Notebook
- Git & GitHub

---

### Principales Hallazgos

- Variabilidad mensual en ventas.
- Diferencias en comportamiento según canal y categoría.
- Distribución del ticket promedio con ligera asimetría positiva.
- Potencial para análisis predictivo futuro.

---

### Estructura del Proyecto

abp_modulo_4/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── src/
│ ├── load_data.py
│ ├── clean_data.py
│ ├── transform_data.py
│ ├── aggregate_data.py
│ └── main.py
│
├── analisis_explicativo.ipynb
└── README.md

---

### Autor: Joselyn Mena Castillo

Ingeniera Civil Industrial  
Proyecto desarrollado para el Bootcamp Fundamentos de la Ingeniería de Datos.