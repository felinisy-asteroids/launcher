from google.cloud import bigquery

schema = [
    bigquery.SchemaField("asteroid_id", "STRING"),
    bigquery.SchemaField("neo_reference_id", "STRING"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("absolute_magnitude_h", "NUMERIC"),
    bigquery.SchemaField("is_potentially_hazardous_asteroid", "BOOLEAN"),
    bigquery.SchemaField("is_sentry_object", "BOOLEAN"),
    bigquery.SchemaField("export_date", "DATE"),
]
