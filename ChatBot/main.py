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
    
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome!"
    
    else:
        return None 
    
def chat():
    tokenizer, model = load_model_and_tokenizer()
    print("Welcome to the ChatBot! You can start chatting. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            # First, check if there's a rule-based response
            response = rule_based_response(user_input)
            if response:
                print("Bot:", response)
            else:
                # If no rule-based response, generate AI response
                ai_response = generate_response(tokenizer, model, user_input)
                print("Bot (AI):", ai_response)

if __name__ == "__main__":
    chat()
