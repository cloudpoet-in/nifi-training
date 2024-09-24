import json
import random
import time
from confluent_kafka import Producer

# Kafka configuration
kafka_conf = {
    'bootstrap.servers': 'localhost:9092'
}



# Initialize the Kafka producer
producer = Producer(kafka_conf)

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.value().decode('utf-8')}")

def generate_measurement():
    # List of possible data sources
    sources = [
        {'type': 'warehouse', 'name': 'Warehouse 1'},
        {'type': 'warehouse', 'name': 'Warehouse 2'},
        {'type': 'city', 'name': 'City Center'},
        {'type': 'city', 'name': 'City Suburb'},
        {'type': 'factory', 'name': 'Factory A'},
        {'type': 'factory', 'name': 'Factory B'}
    ]

    # Randomly select a source
    source = random.choice(sources)

    # Generate random temperature and pressure values
    temperature = round(random.uniform(-20.0, 40.0), 2)  # Random temperature between -20 and 40
    pressure = round(random.uniform(950.0, 1050.0), 2)   # Random pressure between 950 and 1050

    # Create a dictionary with the measurement values and source
    measurement = {
        'source_type': source['type'],
        'source_name': source['name'],
        'temperature': temperature,
        'pressure': pressure,
        'timestamp': int(time.time())
    }

    # Convert the dictionary to a JSON string
    measurement_json = json.dumps(measurement)
    return measurement_json

def main():
    topic = 'nifi-dummy'

    try:
        while True:
            # Generate a random measurement
            measurement = generate_measurement()
            # Send the measurement to the Kafka topic
            producer.produce(topic, value=measurement, callback=acked)
            # Wait for the message to be delivered
            producer.poll(1)
            # Sleep for a specified interval before sending the next message (e.g., 1 second)
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        # Flush any remaining messages in the queue
        producer.flush()

if __name__ == "__main__":
    main()
