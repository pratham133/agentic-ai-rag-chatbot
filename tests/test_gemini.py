from google import genai
from google.genai.errors import ClientError

from config.settings import settings

client = genai.Client(api_key=settings.google_api_key)

models_to_test = [
    "gemini-flash-latest",
    "gemini-pro-latest",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.1-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.0-flash-001",
]

for model in models_to_test:
    print(f"\nTesting: {model}")
    try:
        response = client.models.generate_content(
            model=model,
            contents="Reply with exactly: Hello"
        )
        print("✅ SUCCESS")
        print(response.text)
    except ClientError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ {type(e).__name__}: {e}")