import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
import os
from fuzzywuzzy import process  # Improved string matching

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load FAQ database
with open("faq.json", "r") as file:
    faq_data = json.load(file) #add more data to faq.json as needed

# Preprocess user input
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stopwords.words("english")]
    return " ".join(filtered_tokens)

# Find best match from FAQ data
def get_faq_response(user_query):
    processed_query = preprocess_text(user_query)
    
    # Check for direct matches
    if user_query.lower().strip() in ["hi", "hello", "hey"]:
        return faq_data.get("General Information", {}).get("hi", "Hello! How can I help?")
    
    # Search for best match in FAQ dataset using fuzzy matching
    all_questions = {k: v for category in faq_data.values() for k, v in category.items()}
    best_match, confidence = process.extractOne(processed_query, all_questions.keys())
    
    if confidence > 60:  # Adjust confidence threshold as needed
        return all_questions.get(best_match, "I'm sorry, I don't have an answer for that.")
    
    return "I'm sorry, I don't have an answer for that. Please try asking about business hours, support contact, shipping, or payment methods."

# Clear console for better readability
os.system('cls' if os.name == 'nt' else 'clear')

# Chatbot loop
print("Hello! Ask me a question or type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_faq_response(user_input)
    print(f"Chatbot: {response}")