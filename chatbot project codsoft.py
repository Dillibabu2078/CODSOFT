import re
import random

class ChatBot:
    def __init__(self):
        self.intents = {
            'greeting': r'\b(hi|hello|hey)\b',
            'farewell': r'\b(bye|goodbye|see you|quit|exit)\b',
            'weather': r'what is the weather condition (in|for) (\w+)',
            'name': r'what is (your) name',
            'feeling': r'how (are) (you)',
            'capability': r'(what|who) (can|are) you do',
            'thanks': r'\b(thanks|thank you|thnx)\b',
            'time': r'(what time now|what\'s the time)',
        }
        
        self.responses = {
            'greeting': ["Hello!", "Hi there!", "Greetings!"],
            'farewell': ["Goodbye!", "See you later!", "Take care!"],
            'weather': ["I'm sorry, I don't have real-time weather data for {}. You might want to check a weather app or website."],
            'name': ["My name is ChatBot. Nice to meet you!"],
            'feeling': ["I'm doing well, thank you for asking!", "I'm fine, thanks! How about you?"],
            'capability': ["I'm a chatbot capable of basic conversation. I can discuss weather, time, and answer some simple questions."],
            'thanks': ["You're welcome!", "Glad I could help!", "My pleasure!"],
            'time': ["I'm sorry, I don't have access to real-time clock. You might want to check your device for the current time."],
            'default': ["I'm not sure I understand. Could you rephrase that?", "I didn't quite get that. Can you try asking differently?"]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        
        for intent, pattern in self.intents.items():
            match = re.search(pattern, user_input)
            if match:
                if intent == 'weather':
                    return self.responses[intent][0].format(match.group(2)),False
                elif intent == 'farewell':
                    return random.choice(self.responses[intent]), True
                else:
                    return random.choice(self.responses[intent]), False
        
        return random.choice(self.responses['default']), False

    def chat(self):
        print("ChatBot: Hello! I'm an  chatbot. How can I assist you today?")
        
        while True:
            user_input = input("You: ")
            response, should_exit = self.get_response(user_input)
            print(f"ChatBot: {response}")
            
            if should_exit:
                break

if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()
