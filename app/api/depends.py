from db.session_db import SessionLocal
from broker.session_rabbitMQ import ConnectionBroker
from random import randint

DIGIT = randint(1,10)

def get_digit_header():
    return {"X-random-digit": str(DIGIT)}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_broker():
    broker = ConnectionBroker.channel()
    return broker


