def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("🤖 Chatbot: Hello! How can I help you?")
        elif "your name" in user_input:
            print("🤖 Chatbot: I am a simple Python chatbot.")
        elif "help" in user_input:
            print("🤖 Chatbot: I can answer basic questions. Try saying hello!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

chatbot()