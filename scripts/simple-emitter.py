import paho.mqtt.client as mqtt

broker_host = "localhost"
base_name = "pmcep"
process_name = "test"

traces = []
traces.append(["A", "B", "C"])
traces.append(["A", "B"])
traces.append(["A", "B"])
traces.append(["A", "B"])

c = mqtt.Client()
c.connect(broker_host, 1883, 60)

trace_id = 0
for trace in traces:
    trace_id += 1
    for activity in trace:
        c.publish(base_name + "/" + process_name + "/C" + str(trace_id) + "/" + activity, "{}")
