print("Welcome to Simple Chatbot")
print("Type 'exit' to end the chat")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello"]:
        print("Bot: Hello! How can I help you?")
    elif user == "help":
        print("Bot: You can say hi, hello or exit.")
    elif user == "exit":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
