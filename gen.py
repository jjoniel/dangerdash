import os
import openai
from dotenv import load_dotenv
import json

if __name__ == '__main__':
    load_dotenv()

    openai.api_key = os.getenv('OPENAI_API_KEY')

    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "decision tree for emergency situation FIRE with 2 decisions per step and depth 2. output format: [lively story about scenario;option1;option2;option1.1;option1.2;option2.1;option2.2;outcome1.1;outcome1.2;outcome2.1;outcome2.2;is outcome 1.1 good (1) or bad (0);is outcome 1.2 good (1) or bad (0);is outcome 2.1 good (1) or bad (0);is outcome 2.2 good (1) or bad (0);]. no further info in response."
            }
        ]
    )

    content = {
        "message": completion.choices[0].message.content
    }

    print(completion.choices[0].message)

    with open('saved_variables.json', 'w') as json_file:
        json.dump(content, json_file)
