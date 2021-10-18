import json
import hashlib
from sseclient import SSEClient as EventSource
import paho.mqtt.client as mqtt

wiki_to_process = "itwiki"

broker_host = "broker.hivemq.com"
base_name = "pmcep/wiki"
process_name = wiki_to_process

c = mqtt.Client()
c.connect(broker_host, 1883, 60)
c.loop_start()

url = 'https://stream.wikimedia.org/v2/stream/recentchange'
for event in EventSource(url):
    if event.event == 'message':
        try:
            data = json.loads(event.data)
            activity = data["type"]
            case = hashlib.md5(data["title"].encode()).hexdigest()
            process = data["wiki"]
            if process == wiki_to_process:
                c.publish(base_name + "/" + process_name + "/" + case + "/" + activity, "{}")
                print(".")

        except ValueError:
            pass
