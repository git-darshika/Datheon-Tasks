import json


faq_data = """{
    "hi": "Hello! How can I help you today?",
    "shipping": "Standard shipping takes 3-5 business days.",
    "return": "We offer a 30-day money-back guarantee.",
    "price": "Please visit our website's product page for pricing details."
}"""


intents = json.loads(faq_data)

print("Datheon Chatbot Initialized. Type 'exit' to close.\n")


while True:
    user_input = input("you: ").lower().strip()
    
    
    if user_input in ['bye', 'exit', 'quit']:
        print("Bot: goodbye!")
        break
        
    matched = False
    
    
    for key, response in intents.items():
        if key in user_input:
            print("Bot:", response)
            matched = True
            break
            
    if not matched:
        print("Bot: I don't understand. Ask about shipping, return, or price.")