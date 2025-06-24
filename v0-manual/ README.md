# 🧾 v0 - Manual Execution of Glue Job  
<sub>Ejecución manual del Glue Job</sub>

This version represents the starting point of the ETL process. The Glue Job was manually triggered via AWS Console without any automation.

<details>
  <summary>🇬🇧 English</summary>

## 🎯 Purpose

Process `.csv` sales files uploaded to an S3 bucket, and transform them into Parquet using a Glue Job.

## ⚙️ Technical Details

- **Glue Job**: `Procesar_ventas_S3`
- **Main script**: [`etl_glue_ventas.py`](./scripts/etl_glue_ventas.py)
- **Source**: `s3://<bucket>/raw/`
- **Destination**: `s3://<bucket>/processed/`
- **Execution**: manual, via AWS Glue Studio

## 📂 Structure

```
v0-manual/
├── README.md
└── scripts/
    └── etl_glue_ventas.py
```

## 🧪 Flow

1. Upload a `.csv` file to the bucket
2. Manually run the Glue Job from the console
3. Validate, transform and write results into `/processed/`

## 🚫 Limitations

- Requires human intervention
- Not scalable or schedulable
- No monitoring or observability tools

## 🧭 Evolution

This approach was later replaced by [`v1-lambda`](../v1-lambda/), where an AWS Lambda function triggers the Glue Job automatically upon new file detection.

</details>

<details>
  <summary>🇪🇸 Español</summary>

## 🎯 Objetivo

Procesar archivos `.csv` de ventas cargados en un bucket S3 y transformarlos a Parquet mediante un Glue Job.

## ⚙️ Detalles técnicos

- **Glue Job**: `Procesar_ventas_S3`
- **Script principal**: [`etl_glue_ventas.py`](./scripts/etl_glue_ventas.py)
- **Origen**: `s3://<bucket>/raw/`
- **Destino**: `s3://<bucket>/processed/`
- **Ejecución**: manual desde AWS Glue Studio

## 📂 Estructura

```
v0-manual/
├── README.md
└── scripts/
    └── etl_glue_ventas.py
```

## 🧪 Proceso

1. Subir el archivo `.csv` al bucket
2. Ejecutar el Glue Job desde la consola
3. Validar, transformar y escribir en `/processed/`

## 🚫 Limitaciones

- Requiere intervención manual
- No es escalable ni programable
- Sin trazabilidad ni monitoreo

## 🧭 Evolución

Este flujo fue reemplazado por [`v1-lambda`](../v1-lambda/), donde una función AWS Lambda dispara automáticamente el Glue Job al detectar archivos.

</details>

**AWS Data Engineer**  
AWS Certified (3x): Cloud Practitioner, AI Practitioner, Solutions Architect Associate  
Python | AWS Glue | Lambda | Serverless ETL & Event-Driven Workflows