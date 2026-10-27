
import requests

url = "http://localhost:11434/api/generate"

prompt = """
Create a short educational video script about photosynthesis.
Divide it into 3 scenes.

For each scene, provide:
- Scene title
- Simple narration
- Visual suggestion

Use simple English for school students.
"""

payload = {
    "model": "qwen2.5:3b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload, timeout=120)
response.raise_for_status()

result = response.json()

print("\n--- GENERATED LESSON SCRIPT ---\n")
print(result["response"])
