import os
import openai
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

openai.api_key = os.getenv('OPENAI_API_KEY')

completion = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "say hello world."
        }
    ]
)

print(completion.choices[0].message)

