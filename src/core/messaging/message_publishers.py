from abc import ABC, abstractmethod

class MessagePublisher(ABC):
    @abstractmethod
    def publish(self, topic, message):
        pass
