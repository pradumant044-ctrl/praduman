def chatbot():
    print("Chatbot: Hello! I am your AI chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hi" or user == "hello":
            print("Chatbot: Hello! How can I help you?")
        elif "name" in user:
            print("Chatbot: I am a simple AI chatbot.")
        elif "college" in user:
            print("Chatbot: This chatbot is made for a college AI project.")
        elif user == "bye":
            print("Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("Chatbot: Sorry, I did not understand that.")

chatbot()
