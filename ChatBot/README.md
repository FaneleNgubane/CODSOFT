# ChatBot
This Python project implements a simple conversational agent (ChatBot) using the OpenAI GPT-2 model. The ChatBot engages in conversation with users by responding to their input either based on predefined rules or using AI-generated responses.

# Dependacies 
. Python 3.x
. transformers library

# Installation
To run this project, you need to have Python installed on your system. 
Additionally, you need to install the transformers library. You can install it via pip:
- pip install transformers

# Usage
To use the ChatBot, simply execute the chat() function from the provided Python script.
- python chatbot.py

Once the ChatBot is running, you can start chatting with it. 
Type your message and press Enter to see the Bot's response. Type 'bye' to exit the conversation.

# Features 
. load_model_and_tokenizer(): This function loads the GPT-2 language model and tokenizer from the Hugging Face transformers library. It returns the tokenizer and the model.

. generate_response(tokenizer, model, user_input): This function generates a response using the GPT-2 model. It takes the tokenizer, model, and user input as arguments. It encodes the user input, generates a response, and decodes the output tokens into a readable text.

. rule_based_response(user_input): This function provides predefined rule-based responses. It takes the user input as an argument and returns a response based on specific rules.

. chat(): This is the main function that orchestrates the conversation with the ChatBot. It loads the model and tokenizer, greets the user, and enters a loop to continuously accept user input and provide responses until the user decides to exit by typing "bye".


