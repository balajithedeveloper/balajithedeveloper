# chatbot_memory.py

import os

MEMORY_FILE = "memory.txt"

# Load previous memory
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return file.readlines()
    return []

# Save new conversation
def save_memory(user, bot):
    with open(MEMORY_FILE, "a") as file:
        file.write(f"User: {user}\n")
        file.write(f"Bot: {bot}\n")

# Generate chatbot response
def chatbot_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you?"

    elif "your name" in user_input:
        return "I am a Python chatbot with memory."

    elif "how are you" in user_input:
        return "I am doing great!"

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "I am still learning. Please teach me more."

# Main chatbot loop
def main():

    print("=== Chatbot with Memory ===")
    print("Type 'bye' to exit.\n")

    # Show old memory
    old_memory = load_memory()

    if old_memory:
        print("Previous Conversations:")
        for line in old_memory[-6:]:
            print(line.strip())

        print("\n")

    while True:

        user_input = input("You: ")

        bot_reply = chatbot_response(user_input)

        print("Bot:", bot_reply)

        # Save memory
        save_memory(user_input, bot_reply)

        if "bye" in user_input.lower():
            break

# Run program
main()