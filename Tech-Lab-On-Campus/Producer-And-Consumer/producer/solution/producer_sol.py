import os
import pika
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        self.m_routing_key = routing_key
        self.m_exchange_name = exchange_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.m_connection = pika.BlockingConnection(parameters=con_params)
        self.m_channel = self.m_connection.channel()
        self.m_channel.exchange_declare(self.m_exchange_name)

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.m_channel.basic_publish(self.m_exchange_name,self.m_routing_key,body=message)
        # Close Channel

        # Close Connection
