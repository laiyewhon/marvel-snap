from kafka import KafkaConsumer
import json
import pandas as pd

def start():
    print('Starting tags consumer')
    tags_consumer = KafkaConsumer(
        'in-tags',
        bootstrap_servers=['kafka:9093'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        group_id='out-parquet-tags')

    tags_df = pd.DataFrame()

    for tag in tags_consumer:
        tags_df = tags_df.append(tag.value, ignore_index=True)
        tags_df.to_parquet('data/tags.parquet', engine='fastparquet')