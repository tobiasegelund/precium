import json
from kafka.producer import KafkaProducer
from kafka.errors import NoBrokersAvailable

class MockKafkaProducer:
    pass

try:
    kafka_producer = KafkaProducer(
        value_serializer=lambda msg: json.dumps(msg).encode("utf-8"),
        bootstrap_servers=["localhost:9092"],
    )
except NoBrokersAvailable:
    kafka_producer = MockKafkaProducer()