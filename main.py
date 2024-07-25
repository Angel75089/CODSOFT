def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase
    
    # Simple if-else statements for pattern matching
    if user_input == 'hello' or user_input == 'hi':
        return "Hello! How can I help you today?"
    elif user_input == 'how are you' or user_input == 'how are you doing':
        return "I'm just a bot, but I'm here to help you!"
    elif 'your name' in user_input:
        return "I am a chatbot created by OpenAI."
    elif 'thank you' in user_input or 'thanks' in user_input:
        return "You're welcome!"
    elif user_input == 'bye' or user_input == 'goodbye':
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please ask something else?"

# Main function to run the chatbot
def main():
    print("Welcome! Ask me anything or say goodbye to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye' or user_input.lower() == 'goodbye':
            print(chatbot_response(user_input))
            break
        else:
            print(chatbot_response(user_input))

if __name__ == "__main__":
    main()
