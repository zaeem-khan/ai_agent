import os
from dotenv import load_dotenv
from google import genai
import sys


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    model = "gemini-2.0-flash-001"
    try:
        prompt = sys.argv[1]
        response = client.models.generate_content(model=model, contents=prompt)
    except IndexError:
        print("Error: No Prompt Provided")
        sys.exit(1)

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()