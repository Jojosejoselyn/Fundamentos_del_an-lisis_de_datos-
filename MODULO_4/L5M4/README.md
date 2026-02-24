# Análisis de Caso – Dataset Fintech

## Objetivo
Realizar limpieza, transformación y análisis exploratorio de un dataset de clientes financieros para identificar patrones relevantes en el comportamiento crediticio.

## Procesos Realizados

- Imputación de valores nulos utilizando mediana.
- Eliminación de registros duplicados.
- Identificación de valores extremos mediante método IQR.
- Análisis exploratorio con estadísticas descriptivas.
- Matriz de correlación y visualización con heatmap.
- Análisis segmentado por tipo de cliente.
- Exportación de dataset limpio en formato CSV y Excel.

## Principales Hallazgos

- No se identificaron correlaciones lineales fuertes entre variables financieras.
- El comportamiento de mora no muestra asociación significativa con ingreso o monto de crédito.
- La segmentación por tipo de cliente permite observar diferencias en tasas de mora.

## Archivos del Proyecto

- 01_generacion_dataset_fintech.ipynb
- 02_analisis_caso_data_wrangling.ipynb
- dataset_fintech_sucio.csv
- dataset_fintech_limpio.csv
- dataset_fintech_limpio.xlsx