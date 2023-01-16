from kafka import KafkaConsumer
import json
import pandas as pd

def start():
    print('Starting variants consumer')
    variants_consumer = KafkaConsumer(
        'in-variants',
        bootstrap_servers=['kafka:9093'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        group_id='out-parquet-variants')

    variants_df = pd.DataFrame()

    for variant in variants_consumer:
        variants_df = variants_df.append(variant.value, ignore_index=True)
        variants_df.to_parquet('data/variants.parquet', engine='fastparquet')