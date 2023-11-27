from kafka import KafkaProducer
from core.messaging.message_publisher import MessagePublisher

class KafkaMessagePublisher(MessagePublisher):
    def __init__(self, kafka_producer: KafkaProducer):
        self.kafka_producer = kafka_producer

    def publish(self, topic: str, message: str):
        # Logic to publish a message to the specified Kafka topic
        self.kafka_producer.send(topic, message.encode('utf-8'))

    def close(self):
        # Logic to close the Kafka producer
        self.kafka_producer.close()
