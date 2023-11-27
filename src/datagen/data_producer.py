from faker import Faker
import json
import time

from config.data_producer_config import DataProducerConfig
from infra.kafka.kafka_factory import KafkaFactory
from infra.kafka.kafka_publisher import KafkaMessagePublisher
from utils.data_generator import generate_user_interaction  # Assuming this is a custom utility

class DataProducer:
    def __init__(self, publisher, config):
        self.publisher = publisher
        self.config = config
        self.fake = Faker()

    def produce_data(self):
        while True:
            interaction = generate_user_interaction(self.fake, self.config)
            self.publisher.publish(self.config.kafka_topic, json.dumps(interaction))
            
            # Delay between messages to control the rate of data production
            time.sleep(self.config.delay_between_events)