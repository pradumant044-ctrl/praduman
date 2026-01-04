# Advanced Mini ChatGPT (keyword + memory)
import random

# Pre-defined responses
responses = {
    "hello": ["Hi there!", "Hello! How can I help you?", "Hey!"],
    "how are you": ["I am fine, thank you!", "Doing great! How about you?", "I’m good!"],
    "your name": ["I am MiniChatGPT 🤖", "Call me MiniChatGPT!", "I am your chatbot."],
    "joke": [
        "Why did the computer go to the doctor? Because it caught a virus! 😆",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"
    ],
    "college": [
        "AI is fun for college projects!", 
        "You can use Python to build chatbots for college assignments."
    ],
    "bye": ["Goodbye! Have a nice day 👋", "See you later!", "Bye!"]
}

# Memory to store conversation
conversation_history = []

def get_response(user_input):
    user_input = user_input.lower()
    conversation_history.append(f"You: {user_input}")  # Save user input

    for key in responses:
        if key in user_input:
            reply = random.choice(responses[key])
            conversation_history.append(f"Bot: {reply}")  # Save bot reply
            return reply
    reply = "Sorry, I don't understand that."
    conversation_history.append(f"Bot: {reply}")  # Save unknown reply
    return reply

def chatbot():
    print("Mini ChatGPT started. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print(f"Bot: {reply}")
        if "bye" in user_input.lower():
            break

    # Show conversation history after exit
    print("\n--- Conversation History ---")
    for line in conversation_history:
        print(line)

# Start chatbot
chatbot()