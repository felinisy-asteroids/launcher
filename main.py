import json
import logging
from datetime import datetime, timedelta

from google.cloud import pubsub_v1

from launcher.bigquery_client import bq_client
from utils.helper import get_missing_dates

from utils.settings import settings

logging.basicConfig(level=logging.INFO)


def main(request):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=6)
    bq_client.ensure_table_exists()

    missing_dates = get_missing_dates(start_date, end_date)

    if not missing_dates:
        logging.info("No missing dates found")
        return {'message': "No missing dates found. workflow not started"}, 200

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(settings.PROJECT_ID, settings.TOPIC_ID)

    message_json = {
        "dates": missing_dates
    }

    message_bytes = json.dumps(message_json).encode("utf-8")

    try:
        future = publisher.publish(topic_path, data=message_bytes)
        message_id = future.result()
        logging.info(f"published message {message_id}")
        return {
            "status": "Workflow triggered",
            "dates": missing_dates,
            "pubsub_message_id": message_id
        }, 200
    except Exception as e:
        logging.error("failed to publish message", exc_info=True)
        return {"error": f"failed to publish to pub/sub: {str(e)}"}, 500


if __name__ == "__main__":
    main(1)
