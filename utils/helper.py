from datetime import timedelta

from launcher.bigquery_client import bq_client
from utils.query import select_distinct_export_dates_query


def get_date_range(start_date, end_date) -> list:
    return [(start_date + timedelta(days=x)).strftime("%Y-%m-%d")
            for x in range((end_date - start_date).days + 1)]


def get_missing_dates(start_date, end_date) -> list:
    bq_dates = get_existing_export_dates(start_date, end_date)
    dates = [x for x in get_date_range(start_date, end_date) if x not in bq_dates]
    return dates


def fetch_bigquery_rows(start_date, end_date):
    query = select_distinct_export_dates_query.format(bq_client.table_id, start_date, end_date)
    return bq_client.execute_query(query)


def get_existing_export_dates(start_date, end_date) -> list:
    rows = fetch_bigquery_rows(start_date, end_date)
    return [row.export_date.strftime("%Y-%m-%d") for row in rows]
