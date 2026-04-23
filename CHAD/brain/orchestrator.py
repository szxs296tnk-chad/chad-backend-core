from brain.decision import decide
from execution.queue import enqueue_task

async def handle_request(data):
    decision = decide(data)
    task_id = await enqueue_task(decision)
    return {"task_id": task_id}
