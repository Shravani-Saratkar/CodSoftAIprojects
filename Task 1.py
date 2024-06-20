import re

def chatbot_response(user_input):
    # List of predefined rules with regular expressions
    rules = {
        re.compile(r"hello|hi"): "Hello! How can I help you?",
        re.compile(r"what's your name|who are you"): "I'm a simple chatbot. I don't have a name.",
        re.compile(r"how are you|how's it going"): "I'm just a program, so I don't have feelings. But I'm here to help you. What do you need?",
        re.compile(r"bye|goodbye"): "Goodbye! Have a great day!"
    }

    # Check if user input matches any predefined rule
    for rule, response in rules.items():
        if rule.match(user_input):
            return response

    # If no rule matches, return a default response
    return "I didn't understand that. Can you please rephrase?"

# Test the chatbot
while True:
    user_input = input("You: ")
    print("Chatbot:", chatbot_response(user_input))