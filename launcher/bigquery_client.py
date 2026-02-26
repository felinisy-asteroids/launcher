from google.cloud import bigquery
from google.api_core.exceptions import NotFound

from utils.settings import settings
from launcher.schema import schema


class BigQueryClient:
    def __init__(self):
        self.client = bigquery.Client()
        self.table_id = f"{settings.PROJECT_ID}.{settings.DATASET}.{settings.TABLE_NAME}"

    def execute_query(self, query: str) -> None:
        return self.client.query(query)

    def ensure_table_exists(self) -> None:
        try:
            self.client.get_table(self.table_id)
        except NotFound:
            table = bigquery.Table(self.table_id, schema=schema)
            self.client.create_table(table)


bq_client = BigQueryClient()
