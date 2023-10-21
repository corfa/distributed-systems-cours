import json

from pika.adapters.blocking_connection import BlockingChannel



def put_in_queue(broker: BlockingChannel, url: str, id_: int):
    queue_name = 'new_links'
    broker.queue_declare(queue=queue_name)
    message = {
        'url': url,
        'id': id_
    }
    message_bytes = json.dumps(message).encode('utf-8')
    broker.basic_publish(exchange='', routing_key=queue_name, body=message_bytes)
    broker.close()