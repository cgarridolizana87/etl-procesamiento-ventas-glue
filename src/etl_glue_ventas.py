import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

## 📌 Parámetros del Job
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

## 🔧 Contextos Glue y Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

## 📥 Leer archivo CSV desde S3
input_path = "s3://data-cgarridolizana/raw/ventas.csv"
df = spark.read.option("header", True).csv(input_path)

## 🧪 Transformaciones
df_casted = df \
    .withColumn("cantidad", F.col("cantidad").cast("int")) \
    .withColumn("precio_unitario", F.col("precio_unitario").cast("double")) \
    .withColumn("total_venta", F.col("cantidad") * F.col("precio_unitario"))

## 🧹 Validación / limpieza (por ejemplo: valores nulos)
df_clean = df_casted.dropna(subset=["cantidad", "precio_unitario"])

## 📤 Guardar como Parquet en zona procesada
output_path = "s3://data-cgarridolizana/processed/ventas/"
df_clean.write.mode("overwrite").parquet(output_path)

## ✅ Finalizar Job
job.commit()