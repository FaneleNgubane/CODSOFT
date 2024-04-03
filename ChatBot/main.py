from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model_and_tokenizer():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)
    return tokenizer, model

def generate_response(tokenizer, model, user_input):
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, pad_token_id=tokenizer.eos_token_id)
    
    return tokenizer.decode(output[0], skip_special_tokens=True)

def rule_based_response(user_input):
    user_input = user_input.lower() 
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking!"
    
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a great day!"
    
    elif "help" in user_input:
        return "I can help you with a variety of queries. How can I assist you today?"  
    
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome!"
    
    elif "what is your name" in user_input:
        return "My name is ChatBot."
    
    elif "how old are you" in user_input:
        return "I am an AI, so I don't have an age."
    
    elif "where are you from" in user_input:
        return "I am a virtual assistant, so I don't have a physical location."
    
    elif "what is the meaning of life" in user_input:
        return "The meaning of life is subjective and can vary for each individual."
    
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    
    elif "what is the weather like today" in user_input:
        return "I'm sorry, I don't have access to real-time weather information."
    
    elif "can you recommend a book" in user_input:
        return "Sure! What genre are you interested in?"
    
    elif "how do I create a Python dictionary" in user_input:
        return "You can create a Python dictionary using curly braces {} and key-value pairs."
    
    elif "what is the capital of France" in user_input:
        return "The capital of France is Paris."
    
    elif "how do I install Python" in user_input:
        return "You can download and install Python from the official Python website."
    
    elif "what is the largest planet in our solar system" in user_input:
        return "The largest planet in our solar system is Jupiter."
    
    elif "how do I convert a string to lowercase" in user_input:
        return "You can use the lower() method in Python to convert a string to lowercase."
    
    elif "what is the square root of 16" in user_input:
        return "The square root of 16 is 4."
    
    elif "how do I sort a list in Python" in user_input:
        return "You can use the sort() method or the sorted() function to sort a list in Python."
    
    elif "what is the current time" in user_input:
        return "I'm sorry, I don't have access to real-time clock information."
    
    elif "can you recommend a movie" in user_input:
        return "Sure! What genre are you interested in?"
    
    elif "how do I calculate the factorial of a number" in user_input:
        return "You can use a loop or recursion to calculate the factorial of a number in Python."
    
    elif "what is the capital of Japan" in user_input:
        return "The capital of Japan is Tokyo."
    
    elif "how do I create a virtual environment in Python" in user_input:
        return "You can use the venv module in Python to create a virtual environment."
    
    else:
        return None
    
def chat():
    tokenizer, model = load_model_and_tokenizer()
    print("Welcome to the ChatBot! You can start chatting. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye' or user_input.lower() == 'quit' or user_input.lower() == 'exit':
            print("Bot: Goodbye! Have a great day!")
            break
        else:

            response = rule_based_response(user_input)
            if response:
                print("Bot:", response)
            else:
                ai_response = generate_response(tokenizer, model, user_input)
                print("Bot (AI):", ai_response)

if __name__ == "__main__":
    chat()
