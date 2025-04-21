from google import genai

client = genai.Client(api_key="YOUR GEMINI API KEY HERE")

response = client.models.generate_content(
    model="gemini-2.0-flash-lite", contents="huggingface api keys"
)
print(response.text)
