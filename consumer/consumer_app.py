import pika
import os
import json
from dotenv import load_dotenv
import requests
import redis
import logging

logging.basicConfig(level=logging.INFO) 
load_dotenv()
rabbit_host = os.getenv('RABBIT_HOST', '')
rabbit_port = os.getenv('RABBIT_PORT', '')
rabbit_user = os.getenv('RABBIT_USER','')
rabbit_password = os.getenv('RABBIT_PASSWORD','')

host_app = os.getenv('APP_HOST')

redis_host = os.getenv('REDIS_HOST','')
redis_port = os.getenv('REDIS_PORT','')




r = redis.Redis(host=redis_host, port=redis_port, db=0)

credentials = pika.PlainCredentials(rabbit_user, rabbit_password)

connection_params = pika.ConnectionParameters(rabbit_host, rabbit_port, credentials=credentials) 


connection = pika.BlockingConnection(connection_params)


channel = connection.channel()

channel.queue_declare(queue='new_links')
def callback(ch, method, properties, body):
    try:
        message_dict = json.loads(body.decode('utf-8'))
        url,id_ = message_dict['url'],message_dict['id']

        cached_data = r.get(url)
        if cached_data is not None:
            status = cached_data.decode('utf-8')
            data = {"status":status}
            logging.info('INFO[X] Cache triggered [X]')
        else:
            status = int(requests.get(url).status_code)
            r.setex(url, 3600, status)
            data = {"status":status}
        
        chel_url = f'{host_app}/links/{id_}'
        requests.put(chel_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    except:
        pass
   

channel.basic_consume(queue='new_links', on_message_callback=callback, auto_ack=True)
logging.info("[*] CONSUMER IS START [*]")
channel.start_consuming()
