import os
import pika
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('RABBIT_HOST', '')
port = os.getenv('RABBIT_PORT', '')
username = os.getenv('RABBIT_USERNAME', '')  
password = os.getenv('RABBIT_PASSWORD', '')  

credentials = pika.PlainCredentials('myuser', 'mypassword')


connection_params = pika.ConnectionParameters(
    host=host,
    port=port,
    credentials=credentials,
    heartbeat=1200  
)


ConnectionBroker = pika.BlockingConnection(connection_params)
