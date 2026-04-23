async def echo(payload):
    return {"response": payload}

def get_handler(action):
    if action == "echo":
        return echo
    raise Exception("Unknown action")
