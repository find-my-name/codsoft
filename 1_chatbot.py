print("Hello, I am a chatbot! Start asking your questions.")

while True:
    query = input("User: ")
    if query.lower() in ["hi", "hello", "hey"]:
        print("Bot: Hi! How may I help you?")
    elif query.lower() in ["bye", "see you", "quit"]:
        print("Bot: Goodbye! Feel free to ask any questions.")
        break
    elif query.lower() in ["what is your name?", "how do you call yourself?"]:
        print("Bot: My name is Chatbot. I'm here to assist you with your queries.")
    else:
        print("Bot: I'm not trained to assist with that query.")
