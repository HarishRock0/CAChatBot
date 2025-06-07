import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
nltk.download('punkt_tab')  # Changed from 'punkt' to 'punkt_tab'
nltk.download('stopwords')


# FAQ database
faq_data = {
    "hi": "Hello, how can I help you?",
    "What are your business hours?": "We are open Monday to Friday from 9 AM to 6 PM.",
    "How can I contact support?": "You can reach our support team via email at support@example.com or call +1 234 567 890.",
    "Do you offer international shipping?": "Yes, we offer international shipping to all countries.",
    "What payment methods do you accept?": "We accept credit/debit cards, PayPal, and online banking."
}


# Preprocess user input
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stopwords.words("english")]
    return filtered_tokens


# Find best match from FAQ data
def get_faq_response(user_query):
    processed_query = preprocess_text(user_query)

    # Special case for simple greetings
    if user_query.lower().strip() in ["hi", "hello", "hey"]:
        return faq_data["hi"]

    # Check for keyword matches in FAQ questions
    for question, answer in faq_data.items():
        if question.lower() == "hi":  # Skip the greeting entry for keyword matching
            continue
        # Check if any processed query words appear in the FAQ question
        if any(word in question.lower() for word in processed_query):
            return answer

    return "I'm sorry, I don't have an answer for that. Please try asking about business hours, support contact, shipping, or payment methods."


# Chatbot loop
print("Hello! Ask me a question or type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_faq_response(user_input)
    print(f"Chatbot: {response}")