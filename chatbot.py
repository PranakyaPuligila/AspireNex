import random
import re

class RuleBot:
    negative_res = ("no","nope","nah","not a chance","sorry")
    exit_commands = ("quit","pause","exit","goodbye","bye")

    random_question = (
        "why are you here?"
        "Are there someone like you?"
        "what do you consume tto sustain?"
        "Is there any intelligent life on this planet?"
        "Does earh have a leader?"
    )
    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipaat': r'.*\s*intellipaat.*'
        }
    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am bot. Will you help me to learn about your planet?\n")
        if will_help in self.negative_res:
            print("Have a nice earth day!")
            return
        self.chat()
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Have a nice day")
                return True
    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
    def match_reply(self,reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipaat':
                return self.about_intellipaat()
        if not found_match:
            return self.no_match_intent()
    def describe_planet_intent(self):
        responses = ("My ploanet is a utopia of diverse organism\n",
                     "I heard that the coffee is good here\n")
        return random.choice(responses)
    def answer_why_intent(self):
        responses = ("I am here to collect data on your planet\n")
        return random.choice(responses)
    def about_intellipaat(self):
        responses = ("Intelligence is the world's largest profession\n", 
                     "It will make you learn concept\n", 
                     "It is where your career and skills grows\n")
        return random.choice(responses)
    def no_match_intent(self):
        responses = ("Ple3ase tell me more about this\n", "I see. Can you elaborate\n",
                     "I see. How do you think\n", "why?\n", "How do you think whenI say that and why?\n")
        return random.choice(responses)  

bot = RuleBot()
bot.greet()          
            
        
            
        



