import json

class Parser:
    story = ''
    option1 = {}
    option2 = {}

    def parse(self):
        try:
            with open('saved_variables.json', 'r') as json_file:
                saved_data = json.load(json_file)

                strings = saved_data.get("message")
                print(strings)
                strings = strings.replace('[', '')
                strings = strings.replace(']', '')

                strings = strings.split(';', 40)

                self.story = strings[0]

                self.option1 = {
                    "op1": strings[1],
                    "op1a": strings[3],
                    "op1a_res": strings[7],
                    "op1b": strings[4],
                    "op1b_res": strings[8],
                }

                self.option2 = {
                    "op2": strings[2],
                    "op2a": strings[5],
                    "op2a_res": strings[9],
                    "op2b": strings[6],
                    "op2b_res": strings[10],
                }

                # Printing both dictionaries
                print("Option 1:")
                for key, value in self.option1.items():
                    print(f"{key}: {value}")

                print("\nOption 2:")
                for key, value in self.option2.items():
                    print(f"{key}: {value}")

                answers = strings[11:15]
                print(answers)

        except FileNotFoundError:
            print("No saved variables found.")


