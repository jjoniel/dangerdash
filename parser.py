import json
import os
import openai
from dotenv import load_dotenv

class Parser:
    story = ''
    option1 = {}
    option2 = {}

    def parse(self, emer):
        try:

            load_dotenv()

            openai.api_key = os.getenv('OPENAI_API_KEY')

            completion = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": f"low lexicon vocab kid friendly cheery decision tree for emergency situation {emer} with 2 decisions per step and depth 2. output format: [lively story about scenario;option1;option2;option1pasttense;option2pasttense;option1.1;option1.2;option2.1;option2.2;outcome1.1;outcome1.2;outcome2.1;outcome2.2;is outcome 1.1 good (1) or bad (0);is outcome 1.2 good (1) or bad (0);is outcome 2.1 good (1) or bad (0);is outcome 2.2 good (1) or bad (0);]. no further info in response."
                    }
                ]
            )

            strings = completion.choices[0].message.content
            strings = strings.replace('[', '')
            strings = strings.replace(']', '')
            strings = strings.split(';', 40)

            self.story = strings[0]

            self.option1 = {
                "op1": strings[1],
                "op1_res": strings[3],
                "op1a": strings[5],
                "op1a_res": strings[9],
                "op1b": strings[6],
                "op1b_res": strings[10],
            }

            self.option2 = {
                "op2": strings[2],
                "op2_res": strings[4],
                "op2a": strings[7],
                "op2a_res": strings[11],
                "op2b": strings[8],
                "op2b_res": strings[12],
            }

            # Printing both dictionaries
            print("Option 1:")
            for key, value in self.option1.items():
                print(f"{key}: {value}")

            print("\nOption 2:")
            for key, value in self.option2.items():
                print(f"{key}: {value}")

            answers = strings[13:17]
            print(answers)

        except FileNotFoundError:
            print("No saved variables found.")


