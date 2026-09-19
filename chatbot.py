def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"

    elif "your name" in user_input:
        return "I am a rule-based chatbot created using Python."

    elif "how are you" in user_input:
        return "I am fine! Thank you for asking."

    elif "python" in user_input:
        return "Python is a popular programming language used in AI, ML and Data Science."

    elif "artificial intelligence" in user_input or user_input == "ai":
        return "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."

    elif "internship" in user_input:
        return "This chatbot is Task 1 of my CodSoft Artificial Intelligence Internship."

    elif "help" in user_input:
        return "You can ask me about Python, AI, internship, or my name."

    elif "thank" in user_input:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand. Please try another question."


print("====================================")
print("AI CHATBOT")
print("====================================")
print("Chatbot: Hello! I am your chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break