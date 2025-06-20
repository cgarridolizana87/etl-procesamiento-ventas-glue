# 📄 Notas Técnicas - ETL con AWS Glue 5.0

## ✅ Parámetros clave del Job
- Versión de Glue: 5.0 (Spark 3.5, Python 3.11)
- Formato de salida: Parquet
- Modo de escritura: `overwrite`
- Validación: `dropna` sobre columnas obligatorias

## 🧪 Transformaciones aplicadas
- Casteo de tipos:
  - `cantidad` → Entero
  - `precio_unitario` → Double
- Lógica de negocio:
  - `total_venta = cantidad × precio_unitario`
- Limpieza:
  - Eliminación de filas nulas en columnas críticas

## 🛠️ Buenas prácticas implementadas
- Enforzamiento de tipos
- Separación entre zonas raw y processed
- Transformaciones claramente documentadas

## 🪵 Errores comunes resueltos
- Errores de casteo en Spark
- Campos nulos que provocaban excepciones Py4J
- Desajustes de región al escribir en S3

## 📂 Ubicaciones S3
- Zona RAW: `s3://data-cgarridolizana/raw/ventas.csv`
- Zona PROCESADA: `s3://data-cgarridolizana/processed/ventas/`