Create a simple chatboat
import random

def greet():
    responses = ["Hello!", "Hi there!", "Greetings!", "Hey! How can I help you today?"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Farewell!", "Have a great day!"]
    return random.choice(responses)

def respond_to_question(question):
    question = question.lower()

    if "how are you" in question:
        return "I'm just a computer program, but I'm doing well. Thanks for asking!"
    elif "your name" in question:
        return "I'm a chatbot, you can call me ChatGPT."
    elif "hello" in question or "hi" in question:
        return greet()
    elif "goodbye" in question or "bye" in question:
        return farewell()
    else:
        return "I'm sorry, I don't understand that question."

def chat():
    print("Chatbot: " + greet())

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: " + farewell())
            break

        response = respond_to_question(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    print("Welcome to the Simple Chatbot!")
    chat()

