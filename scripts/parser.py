import json

def filter_logs(logs):
    for log in logs:
        msg = log['message']
        idx = msg.find('[Tracker]')
        if idx != -1:
            return msg[idx+9:-1]
    return -1

def to_json(data):
    return json.dumps(data, indent=2)