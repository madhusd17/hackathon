import requests
import json
import time

prompt = """You are an educational script writer.
Topic: Photosynthesis
Language: Hindi
Output ONLY a JSON object:
{
  "title": "प्रकाश संश्लेषण (Photosynthesis)",
  "level": "beginner",
  "language": "hi",
  "scenes": [
    {
      "type": "title_card",
      "heading": "प्रकाश संश्लेषण क्या है?",
      "subheading": "पौधों का भोजन बनाने का तरीका",
      "narration": "प्रकाश संश्लेषण वह प्रक्रिया है जिससे पौधे अपना भोजन बनाते हैं।"
    },
    {
      "type": "diagram",
      "heading": "मुख्य घटक",
      "items": ["सूर्य का प्रकाश", "पानी (Water)", "कार्बन डाइऑक्साइड (CO2)"],
      "narration": "पौधे सूर्य की रोशनी, पानी और कार्बन डाइऑक्साइड का उपयोग करते हैं।"
    },
    {
      "type": "summary",
      "heading": "परिणाम",
      "items": ["ग्लूकोज (ऊर्जा)", "ऑक्सीजन (जीवन)"],
      "narration": "इस प्रक्रिया से ग्लूकोज बनता है और ऑक्सीजन हवा में निकलती है।"
    }
  ]
}
Return valid JSON only:"""

t0 = time.time()
res = requests.post('http://localhost:11434/api/generate', json={
    'model': 'qwen2.5:3b',
    'prompt': prompt,
    'stream': False,
    'format': 'json',
    'options': {'temperature': 0.3}
}, timeout=60)
print(f"Time taken: {time.time() - t0:.2f}s")
data = res.json()
print("Response:")
print(data.get('response'))

