import boto3

# Nombre fijo del Glue Job de Cristobal
GLUE_JOB_NAME = "Procesar_ventas_S3"

def lambda_handler(event, context):
    glue = boto3.client("glue")
    
    try:
        # Extraer detalles del archivo subido a S3
        record = event["Records"][0]
        s3_bucket = record["s3"]["bucket"]["name"]
        s3_key = record["s3"]["object"]["key"]

        # Validar ubicación esperada: raw/*.csv
        if not s3_key.startswith("raw/") or not s3_key.endswith(".csv"):
            print(f"[SKIP] Archivo ignorado: {s3_key}")
            return {"statusCode": 204, "body": "Archivo fuera de patrón esperado"}

        print(f"[INFO] Archivo detectado: s3://{s3_bucket}/{s3_key}")

        # Ejecutar el Glue Job pasando parámetros opcionales
        response = glue.start_job_run(
            JobName=GLUE_JOB_NAME,
            Arguments={
                "--bucket_name": s3_bucket,
                "--object_key": s3_key
            }
        )

        run_id = response["JobRunId"]
        print(f"[SUCCESS] Glue Job iniciado. Run ID: {run_id}")

        return {
            "statusCode": 200,
            "body": f"Glue Job ejecutado correctamente. Run ID: {run_id}"
        }

    except Exception as e:
        print(f"[ERROR] Falló la ejecución: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Error al iniciar Glue Job: {str(e)}"
        }