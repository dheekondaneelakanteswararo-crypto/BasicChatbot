from datetime import datetime

CHAT_HISTORY = "chat_history.txt"



def save_chat(user, bot):

    with open(CHAT_HISTORY, "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]\n")
        file.write(f"You : {user}\n")
        file.write(f"Bot : {bot}\n\n")


def chatbot_response(message):

    message = message.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey"]:
        return "👋 Hello! Welcome to CodeAlpha Chatbot."

    elif message == "good morning":
        return "🌞 Good Morning! Have a wonderful day."

    elif message == "good afternoon":
        return "☀️ Good Afternoon!"

    elif message == "good evening":
        return "🌙 Good Evening!"

    # Basic Conversation
    elif message == "how are you":
        return "😊 I'm doing great! Thanks for asking."

    elif message == "what is your name":
        return "🤖 I am CodeAlpha Rule-Based Chatbot."

    elif message == "who created you":
        return "👨‍💻 I was created as part of the CodeAlpha Python Internship."

    elif message == "what can you do":
        return ("I can:\n"
                "- Greet you\n"
                "- Tell date & time\n"
                "- Answer simple questions\n"
                "- Save chat history\n"
                "- Exit safely")

    # Date & Time
    elif message == "time":
        return datetime.now().strftime("Current Time: %I:%M:%S %p")

    elif message == "date":
        return datetime.now().strftime("Today's Date: %d-%m-%Y")

    # Help
    elif message == "help":
        return (
            "Available Commands:\n"
            "hello\n"
            "how are you\n"
            "time\n"
            "date\n"
            "what is your name\n"
            "who created you\n"
            "what can you do\n"
            "bye"
        )

    # Exit
    elif message in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    # Unknown
    else:
        return "❌ Sorry, I don't understand that. Type 'help'."


def main():

    print("=" * 55)
    print("      CodeAlpha Rule-Based Chatbot")
    print("=" * 55)

    print("\nType 'help' to see available commands.")
    print("Type 'bye' to exit.\n")

    while True:

        user = input("You : ")

        bot = chatbot_response(user)

        print("Bot :", bot)

        save_chat(user, bot)

        if user.lower() in ["bye", "exit", "quit"]:
            print("\nChat history saved successfully.")
            print("Thank you for using CodeAlpha Chatbot.")
            break


if __name__ == "__main__":
    main()