import json

text = input('Enter JSON data, for example {"name": "Asha"}: ')

try:
    data = json.loads(text)
    print("Decoded data:", data)
except json.JSONDecodeError:
    print("The text is not valid JSON")
