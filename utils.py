"""
=========================================
utils.py

Utility Functions
=========================================
"""

from datetime import datetime

CHAT_HISTORY = "chat_history.txt"


def welcome_message():

    hour = datetime.now().hour

    if hour < 12:
        greeting = "🌞 Good Morning"

    elif hour < 17:
        greeting = "☀️ Good Afternoon"

    else:
        greeting = "🌙 Good Evening"

    print("=" * 60)
    print("        CodeAlpha AI Assistant")
    print("=" * 60)
    print(greeting)
    print("I'm a Rule-Based AI Chatbot.")
    print("\nType 'help' to see all commands.")
    print("Type 'bye' to exit.")
    print("=" * 60)


def save_chat(user, bot):

    with open(CHAT_HISTORY, "a", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write(
            f"Time : {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n"
        )
        file.write(f"You : {user}\n")
        file.write(f"Bot : {bot}\n")
        file.write("=" * 60 + "\n\n")