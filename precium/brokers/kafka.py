import json
from kafka.producer import KafkaProducer


kafka_producer = KafkaProducer(
    value_serializer=lambda msg: json.dumps(msg).encode("utf-8"),
    bootstrap_servers=["localhost:9092"],
)
