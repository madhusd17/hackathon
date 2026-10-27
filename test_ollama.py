import requests
import json
import time

prompt = """You are an expert teacher creating a short visual lesson.
Topic: How does a Python loop work?
Level: beginner
Language: en
Target scenes: 3-4

Generate a valid JSON object only (no markdown, no backticks, no extra text):
{
  "title": "How a Python loop works",
  "level": "beginner",
  "language": "en",
  "scenes": [
    {
      "type": "title_card",
      "heading": "How does a Python loop work?",
      "subheading": "Repeating tasks made simple",
      "narration": "A loop repeats an instruction for each item in a sequence."
    },
    {
      "type": "code_walkthrough",
      "heading": "Writing the Loop",
      "code": "for i in range(3):\\n    print(i)",
      "highlight_lines": [1],
      "narration": "The for loop counts through the numbers zero, one, and two."
    },
    {
      "type": "diagram",
      "heading": "Loop Iterations",
      "items": ["Iteration 0: i = 0", "Iteration 1: i = 1", "Iteration 2: i = 2"],
      "narration": "In each step, i takes the next value and prints it on screen."
    }
  ]
}
Output valid JSON:"""

t0 = time.time()
res = requests.post('http://localhost:11434/api/generate', json={
    'model': 'qwen2.5:3b',
    'prompt': prompt,
    'stream': False,
    'format': 'json',
    'options': {'temperature': 0.3}
}, timeout=120)
dt = time.time() - t0
print(f"Time taken: {dt:.2f}s")
data = res.json()
print("Response:")
parsed = json.loads(data['response'])
print(json.dumps(parsed, indent=2))
