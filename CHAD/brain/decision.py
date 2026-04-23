def decide(data):
    return {
        "action": data.get("action", "echo"),
        "payload": data
    }
