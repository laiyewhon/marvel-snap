FROM python:3.10

RUN pip install pandas kafka-python fastparquet

RUN mkdir /app

WORKDIR /app

COPY consumercard.py /app/consumercard.py
COPY consumertags.py /app/consumertags.py
COPY consumervariants.py /app/consumervariants.py
COPY kafka-consumers.py /app/kafka-consumers.py

CMD ["python", "kafka-consumers.py"]
