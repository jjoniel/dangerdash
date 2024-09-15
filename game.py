import os
import openai
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

openai.api_key = os.getenv('OPENAI_API_KEY')

# completion = openai.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "say hello world."
#         }
#     ]
# )

# print(completion.choices[0].message)

import tkinter as tk
from PIL import ImageTk, Image

class EmergencyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emergency Preparedness for Kids")
        self.root.geometry("800x600")
        self.root.configure(bg="#ADD8E6")  # Light blue background

        self.create_main_menu()

    def create_main_menu(self):
        # Main menu title
        self.title = tk.Label(self.root, text="Learn What To Do In Emergencies!", font=("Arial", 24, "bold"), bg="#ADD8E6")
        self.title.pack(pady=20)

        # Button frame to hold emergency buttons
        self.button_frame = tk.Frame(self.root, bg="#ADD8E6")
        self.button_frame.pack(pady=20)

        # Fire Emergency Button
        fire_img = ImageTk.PhotoImage(Image.open("fire.png").resize((300, 300)))
        self.fire_button = tk.Button(self.button_frame, image=fire_img, command=self.fire_emergency, bg="#ADD8E6")
        self.fire_button.image = fire_img  # Keep a reference
        fire_label = tk.Label(self.button_frame, text="Fire", font=("Arial", 14), bg="#ADD8E6")

        # Earthquake Emergency Button
        earthquake_img = ImageTk.PhotoImage(Image.open("earthquake.png").resize((300, 300)))
        self.earthquake_button = tk.Button(self.button_frame, image=earthquake_img, command=self.earthquake_emergency, bg="#ADD8E6")
        self.earthquake_button.image = earthquake_img
        earthquake_label = tk.Label(self.button_frame, text="Earthquake", font=("Arial", 14), bg="#ADD8E6")

        # Stranger Danger Button
        stranger_img = ImageTk.PhotoImage(Image.open("stranger.png").resize((300, 300)))
        self.stranger_button = tk.Button(self.button_frame, image=stranger_img, command=self.stranger_danger, bg="#ADD8E6")
        self.stranger_button.image = stranger_img
        stranger_label = tk.Label(self.button_frame, text="Stranger Danger", font=("Arial", 14), bg="#ADD8E6")

        # Layout
        self.fire_button.grid(row=0, column=0, padx=20, pady=10)
        fire_label.grid(row=1, column=0)
        self.earthquake_button.grid(row=0, column=1, padx=20, pady=10)
        earthquake_label.grid(row=1, column=1)
        self.stranger_button.grid(row=0, column=2, padx=20, pady=10)
        stranger_label.grid(row=1, column=2)

    # Helper function to hide main menu
    def hide_main_menu(self):
        self.title.pack_forget()
        self.button_frame.pack_forget()

    # Function to show the emergency information on the same screen
    def show_emergency_info(self, title, message, image_file):
        self.hide_main_menu()  # Hide the main menu

        # Display emergency info
        self.info_title = tk.Label(self.root, text=title, font=("Arial", 20, "bold"), bg="#FFFACD")
        self.info_title.pack(pady=10)

        img = ImageTk.PhotoImage(Image.open(image_file).resize((200, 200)))
        self.img_label = tk.Label(self.root, image=img, bg="#FFFACD")
        self.img_label.image = img  # Keep a reference to the image
        self.img_label.pack(pady=10)

        self.info_message = tk.Label(self.root, text=message, font=("Arial", 14), bg="#FFFACD", justify="left")
        self.info_message.pack(pady=10)

        # Back button to return to main menu
        self.back_button = tk.Button(self.root, text="Back to Menu", command=self.back_to_menu, bg="#FFB6C1", font=("Arial", 12, "bold"))
        self.back_button.pack(pady=10)

    # Back to main menu function
    def back_to_menu(self):
        # Hide the emergency info
        self.info_title.pack_forget()
        self.img_label.pack_forget()
        self.info_message.pack_forget()
        self.back_button.pack_forget()

        # Show the main menu again
        self.create_main_menu()

    # Functions for each emergency
    def fire_emergency(self):
        self.show_emergency_info(
            "Fire Emergency",
            "If there is a fire:\n\n1. Stay low to avoid smoke.\n2. Leave the building quickly.\n3. Do not use elevators.\n4. Call 911 once safe.",
            "fire.png"
        )

    def earthquake_emergency(self):
        self.show_emergency_info(
            "Earthquake Emergency",
            "If there is an earthquake:\n\n1. Drop to the ground.\n2. Take cover under sturdy furniture.\n3. Hold on until shaking stops.",
            "earthquake.png"
        )

    def stranger_danger(self):
        self.show_emergency_info(
            "Stranger Danger",
            "If approached by a stranger:\n\n1. Stay away and don't talk.\n2. Yell for help.\n3. Find a trusted adult.",
            "stranger.png"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = EmergencyApp(root)
    root.mainloop()
