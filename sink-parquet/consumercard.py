from kafka import KafkaConsumer
import json
import pandas as pd

def start():
    print('Starting cards consumer')
    card_consumer = KafkaConsumer(
        'in-cards',
        bootstrap_servers=['kafka:9093'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        group_id='out-parquet-cards')

    card_df = pd.DataFrame()

    for card in card_consumer:
        card_df = card_df.append(card.value, ignore_index=True)
        card_df.to_parquet('data/cards.parquet', engine='fastparquet')