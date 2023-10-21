import pika

import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('RABBIT_HOST', '')
port = os.getenv('RABBIT_PORT', '')
username = os.getenv('RABBIT_USERNAME', '')  # Имя пользователя
password = os.getenv('RABBIT_PASSWORD', '')  # Пароль

credentials = pika.PlainCredentials('myuser', 'mypassword')
ConnectionBroker = pika.BlockingConnection(pika.ConnectionParameters(host, port, credentials=credentials))
