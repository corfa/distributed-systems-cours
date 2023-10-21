import pika
import os
import json
from dotenv import load_dotenv
import requests
load_dotenv()
rabit_host = os.getenv('RABBIT_HOST', '')
rabit_port = os.getenv('RABBIT_PORT', '')
rabit_user = os.getenv('RABBIT_USER','')
rabbit_password = os.getenv('RABBIT_PASSWORD','')

host_app = os.getenv('APP_HOST')

credentials = pika.PlainCredentials(rabit_user, rabbit_password)

connection_params = pika.ConnectionParameters(rabit_host,rabit_port,credentials=credentials) 


connection = pika.BlockingConnection(connection_params)


channel = connection.channel()


channel.queue_declare(queue='new_links')

def callback(ch, method, properties, body):
    try:
        message_dict = json.loads(body.decode('utf-8'))
        url,id_ = message_dict['url'],message_dict['id']
        data = {"status":int(requests.get(url).status_code)}
        chel_url = f'{host_app}/links/{id_}'
        requests.put(chel_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    except:
        pass
   

channel.basic_consume(queue='new_links', on_message_callback=callback, auto_ack=True)
print("[*] CONSUMER IS START [*]")
channel.start_consuming()
