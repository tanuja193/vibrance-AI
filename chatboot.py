import nltk
import random
from nltk.chat.util import Chat, reflections
# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatty and I'm a chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created you?",
        ["My Creator is JARVIS",]
    ],
]
def chatbot():
    print("Hi! I'm Chatty the Chatbot and I like to chat :)")
    print("Please type in English language.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
