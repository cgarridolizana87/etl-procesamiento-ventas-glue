# 🚀 ETL Sales Pipeline with AWS Glue 5.0

| Language | Idioma |
|----------|--------|
| 🇺🇸 English | [Español](#-pipeline-de-procesamiento-de-ventas-con-aws-glue-50) |

---

This project implements an AWS Glue 5.0 ETL job to transform raw sales data stored as CSV files in S3 into clean, structured Parquet files. It applies safe type casting, validation, and the calculation of a derived metric (`total_venta`). Designed as a foundational component for modern analytics pipelines.

## 🧱 Stack

- AWS Glue 5.0 (Spark 3.5, Python 3.11)
- Amazon S3
- PySpark
- Parquet output
- Compatible with Lambda, Airflow, Redshift

## ⚙️ ETL Logic

- **Input**: `s3://data-cgarridolizana/raw/ventas.csv`
- **Transformations**:
  - Cast `cantidad` → `int`
  - Cast `precio_unitario` → `double`
  - Compute `total_venta = cantidad × precio_unitario`
  - Filter invalid rows
- **Output**: `s3://data-cgarridolizana/processed/ventas/` as Parquet

## 📌 Sample Code

```python
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
job.init(args["JOB_NAME"], args)
df = df.withColumn("total_venta", F.col("cantidad") * F.col("precio_unitario"))
df_clean.write.mode("overwrite").parquet("s3://.../processed/ventas/")
```

## 🌐 Next Steps

- Trigger via AWS Lambda (event-driven)
- Orchestrate with Apache Airflow
- Load into Amazon Redshift
- Visualize with Power BI or QuickSight

---

## 🇪🇸 Pipeline de Procesamiento de Ventas con AWS Glue 5.0

Este proyecto implementa un Job de Glue 5.0 que transforma datos crudos de ventas (en formato CSV en S3) en archivos Parquet estructurados y limpios. Aplica casteo seguro de tipos, validación, cálculo de la métrica derivada `total_venta`, y está preparado para integrarse a un pipeline analítico moderno.

## 🧱 Tecnologías

- AWS Glue 5.0 (Spark 3.5, Python 3.11)
- Amazon S3
- PySpark
- Parquet optimizado
- Compatible con Lambda, Airflow y Redshift

## ⚙️ Lógica del ETL

- **Entrada**: `s3://data-cgarridolizana/raw/ventas.csv`
- **Transformaciones**:
  - Cast `cantidad` → `int`
  - Cast `precio_unitario` → `double`
  - Cálculo: `total_venta = cantidad × precio_unitario`
  - Filtro de registros inválidos
- **Salida**: `s3://data-cgarridolizana/processed/ventas/` en Parquet

## 📌 Fragmento de Código

```python
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
job.init(args["JOB_NAME"], args)
df = df.withColumn("total_venta", F.col("cantidad") * F.col("precio_unitario"))
df_clean.write.mode("overwrite").parquet("s3://.../processed/ventas/")
```

## 🌐 Próximos pasos

- Activador automático con AWS Lambda  
- Orquestación con Apache Airflow  
- Carga a Redshift para análisis  
- Visualización con Power BI o QuickSight
 ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​   ​
