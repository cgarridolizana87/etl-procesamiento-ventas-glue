# 🚀 ETL Sales Pipeline with AWS Glue 5.0

![AWS Certified](https://img.shields.io/badge/AWS%20Certified-3x-232f3e?logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![AWS Glue](https://img.shields.io/badge/AWS%20Glue-ETL-orange?logo=amazonaws)
![Lambda](https://img.shields.io/badge/AWS%20Lambda-Serverless-ff9900?logo=amazonaws)
![Last Commit](https://img.shields.io/github/last-commit/cgarridolizana87/etl-procesamiento-ventas-glue)

Este proyecto implementa un job de AWS Glue 5.0 para transformar datos crudos de ventas (CSV en S3) en archivos Parquet estructurados. Aplica casteo seguro, validación y cálculo de la métrica `total_venta`. Diseñado como base para pipelines analíticos modernos.

---

## 🌐 Idioma / Language

Este repositorio es bilingüe. La documentación está disponible en español e inglés.  
This repository is bilingual. Documentation is available in Spanish and English.

---

## 🗂️ Versiones del Proyecto

| Versión       | Descripción                                                                 |
|---------------|------------------------------------------------------------------------------|
| `v0-manual/`  | Versión local con PySpark, ejecutada manualmente                            |
| `v1-lambda/`  | Versión serverless con AWS Lambda y Glue como job automatizado              |
| `v2-airflow/` | (Próximamente) Orquestación con Apache Airflow y ejecución programada       |

---

## ⚙️ Tecnologías utilizadas

- AWS Glue 5.0 (Spark 3.5, Python 3.11)
- Amazon S3
- AWS Lambda
- PySpark
- Parquet
- (Preparado para Airflow, Redshift, QuickSight)

---

## 🔄 Lógica del ETL

**Entrada:**  
`s3://data-cgarridolizana/raw/ventas.csv`

**Transformaciones:**
- Cast `cantidad` → `int`
- Cast `precio_unitario` → `double`
- Calcular `total_venta = cantidad × precio_unitario`
- Filtrar registros inválidos

**Salida:**  
`s3://data-cgarridolizana/processed/ventas/` como archivos Parquet

---

## 🧪 Fragmento de código

```python
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
job.init(args["JOB_NAME"], args)

df = df.withColumn("total_venta", F.col("cantidad") * F.col("precio_unitario"))
df_clean.write.mode("overwrite").parquet("s3://.../processed/ventas/")
```

---

## 🚀 Próximos pasos

- Activador automático con AWS Lambda
- Orquestación con Apache Airflow
- Carga a Amazon Redshift
- Visualización con Power BI o QuickSight

---

## 🙋‍♂️ Autor

**Cristobal Garrido L.**  
AWS Data Engineer  
AWS Certified (3x): Cloud Practitioner, AI Practitioner, Solutions Architect Associate  
Python | AWS Glue | Lambda | Serverless ETL & Event-Driven Workflows