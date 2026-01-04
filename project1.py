
    

while True:
    user = input("You: ").lower()  # Converts input to lowercase

    if user == "hello":
        print("Bot: Hello! How can I help you?")
    elif user == "how are you":
        print("Bot: I am fine 😊")
    elif user == "what is your name":
        print("Bot: I am your AI chatbot 🤖")
    elif user == "tell me a joke":
        print("Bot: Why did the computer go to the doctor? Because it caught a virus! 😆")
    elif user == "exit":
        print("Bot: Goodbye 👋")
        break
    else:
        print("Bot: Sorry, I don't understand.")
        
