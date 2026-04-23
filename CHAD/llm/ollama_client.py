import requests

def query(prompt):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "gemma", "prompt": prompt}
    )
    return r.json()
