import uuid

# Placeholder queue (replace with Redis later)
async def enqueue_task(task):
    task_id = str(uuid.uuid4())
    # send to queue system
    return task_id
