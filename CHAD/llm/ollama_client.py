import requests

BASE_URL = "https://reno-generations-terrain-mild.trycloudflare.com"

def query(prompt, model="gemma:2b"):
    r = requests.post(
        f"{BASE_URL}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )
    return r.json()
