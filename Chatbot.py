from textblob import TextBlob
import random
sents = []
def chatbot():
    print("\n--------------Your Daily Happiness Verifier---------------\n")
    name = str(input("Hi, Who are You?\n"))
    name_responses = ["Oh Hi {}, Have a great day", "Hello {}, You are going to have a wonderful day ahead!","Hi {} dear, I am so glad to meet you!"]
    print(random.choice(name_responses).format(name))
    sentiment()

def sentiment():
    print("Share your Experience with me?")
    experience = str(input())
    sents.append(TextBlob(experience).sentiment.polarity)
    print(sents[-1])
    interest = str(input("Do you  want to share another Experience?(Yes/No)"))
    if interest == "No" or interest == "no":
        sent = sum(sents)/len(sents)
        if sent >= 0.5:
            print("So far you have a great experience today")
            print("Try to be more cheerful and have a great day!")
        else:
            print("Oh no, Today you have a bad day")
            print("It's Okay to have a bad day. Learn lessons from today's experience to plan a great day")
    elif interest == 'Yes' or 'yes':
        sentiment()
        
        
