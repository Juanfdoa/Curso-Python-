import random

responses = {
    ("hello", "hi", "hey", "howdy", "greetings"): [
        "Hello! How can I help you?",
        "Hey there! What can I do for you?",
        "Hi! Good to see you. How can I assist?",
    ],
    ("how are you", "how's it going", "how do you do", "what's up"): [
        "I'm doing great, thanks for asking! How about you?",
        "All good on my end! How are you?",
    ],
    ("your name", "who are you", "what are you"): [
        "I'm Chatbot, your virtual assistant!",
        "My name is Chatbot. Nice to meet you!",
    ],
    ("joke", "tell me something funny", "make me laugh"): [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call a fish without eyes? A fsh!",
    ],
    ("help", "what can you do", "commands"): [
        "I can chat with you, tell jokes, and answer basic questions. Give it a try!",
    ],
    ("thanks", "thank you", "appreciate it"): [
        "You're welcome! Happy to help.",
        "Anytime! Is there anything else I can do for you?",
    ],
    ("bye", "goodbye", "see you", "later", "farewell"): [
        "Goodbye! It was nice chatting with you.",
        "See you later! Have a wonderful day!",
    ],
}

EXITS = {"bye", "goodbye", "see you", "later", "farewell", "exit", "quit"}


def get_response(user_input):
    user_input = user_input.lower().strip()

    for keys, options in responses.items():
        if any(key in user_input for key in keys):
            return random.choice(options)

    return "Hmm, I didn't quite get that. Try rephrasing? (type 'help' to see what I can do)"


def chatbot():
    print("=" * 45)
    print("  Chatbot — type 'exit' to quit")
    print("=" * 45)
    print()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in EXITS:
            print("Chatbot:", random.choice(responses[("bye", "goodbye", "see you", "later", "farewell")]))
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}\n")


if __name__ == "__main__":
    chatbot()