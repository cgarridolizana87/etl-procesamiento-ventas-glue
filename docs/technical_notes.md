# 📄 Technical Notes - ETL with AWS Glue 5.0

## ✅ Key Job Parameters
- Glue Version: 5.0 (Spark 3.5, Python 3.11)
- Output format: Parquet
- Write mode: `overwrite`
- Validation: `dropna` on critical columns

## 🧪 Transformations Applied
- Type casting:
  - `cantidad` → Integer
  - `precio_unitario` → Double
- Business logic:
  - `total_venta = cantidad * precio_unitario`
- Data cleaning:
  - Dropping null rows in critical columns

## 🛠️ Best Practices Implemented
- Explicit schema enforcement (type safety)
- Raw vs. Processed S3 separation
- Column transformations documented for reproducibility

## 🪵 Common Issues Resolved
- Spark type mismatches (cast errors)
- Null fields causing Py4J exceptions
- Region mismatch during S3 writing

## 📂 File Paths
- Raw zone: `s3://data-cgarridolizana/raw/ventas.csv`
- Processed zone: `s3://data-cgarridolizana/processed/ventas/`