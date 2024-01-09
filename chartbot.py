from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot('My ChatBot')


trainer = ListTrainer(chatbot)
conversations = [
    "Hello, how are you?",
    "I'm a chatbot, I don't have feelings.",
    "What is your purpose?",
    "My purpose is to assist and help you.",
    "Can you help me with something?",
    "Yes, I can try my best to help you.",
]
trainer.train(conversations)


response = chatbot.get_response("What can you do?")
print(response)
