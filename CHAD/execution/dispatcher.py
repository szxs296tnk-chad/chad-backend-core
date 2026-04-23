from execution.registry import get_handler

async def dispatch(task):
    handler = get_handler(task["action"])
    return await handler(task["payload"])
