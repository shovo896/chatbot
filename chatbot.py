import random
import re
import xml.etree.ElementTree as ET

def load_intents(path="intents.xml"):
    tree = ET.parse(path)
    root = tree.getroot()
    intents = []

    for intent in root.findall("intent"):
        tag = intent.find("tag").text
        patterns = [p.text for p in intent.find("patterns").findall("pattern")]
        responses = [r.text for r in intent.find("responses").findall("response")]
        intents.append({"tag": tag, "patterns": patterns, "responses": responses})

    return intents

def preprocess(text):
    return re.sub(r"[^\w\s]", "", text.lower())

def get_response(user_input, intents):
    user_input = preprocess(user_input)
    for intent in intents:
        for pattern in intent["patterns"]:
            if preprocess(pattern) in user_input:
                return random.choice(intent["responses"])
    return "Sorry, I didn't understand that."

def main():
    intents = load_intents()
    print(" SmartChatXML: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("SmartChatXML: Goodbye!")
            break
        response = get_response(user_input, intents)
        print("SmartChatXML:", response)

if __name__ == "__main__":
    main()

