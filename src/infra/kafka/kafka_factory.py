from kafka import KafkaProducer
from config.kafka_config import KafkaConfig

class KafkaFactory:
    @staticmethod
    def create_kafka_producer(config: KafkaConfig) -> KafkaProducer:
        # Create and return a KafkaProducer instance based on the provided configuration
        return KafkaProducer(
            bootstrap_servers=config.bootstrap_servers,
            # Additional Kafka producer configuration parameters can be added here
        )
