import re
from datetime import datetime

def chatbot():
    print("SimpleChatBot: Hi! I can respond to greetings, time, weather (mocked), and jokes.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["quit", "bye", "exit"]:
            print("SimpleChatBot: Goodbye!")
            break
        elif re.match(r"hi|hello|hey", user_input):
            print("SimpleChatBot: Hello there!")
        elif "time" in user_input:
            print("SimpleChatBot:", datetime.now().strftime("Current time is %I:%M %p"))
        elif "weather" in user_input:
            match = re.search(r"weather.*in ([a-zA-Z\s]+)", user_input)
            if match:
                city = match.group(1).title()
                print(f"SimpleChatBot: It's always sunny in {city} with 25°C!")  # Mock response
            else:
                print("SimpleChatBot: Ask like 'what's the weather in Delhi?'")
        elif "joke" in user_input:
            print("SimpleChatBot: Why don’t scientists trust atoms? Because they make up everything!")
        else:
            print("SimpleChatBot: I didn't get that. Try asking about time, weather, or say hi.")

if __name__ == "__main__":
    chatbot()
