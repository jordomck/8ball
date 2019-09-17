
import random
def getQuestion():
    question = input("What is your question? ")
    if(question == "quit"):
        exit()
    
    return question

def checkQuestion(question):
    isQuestion = question[-1] == '?'
    if not isQuestion:
        print("I'm sorry, I can only answer questions.")
    return isQuestion

def getanswers():
    answers= ['It is certain.','It is decidedly so.','Without a doubt.','Yes - definitely.',
    'You may rely on it.','As I see it, yes.','Most likely.','Outlook good.','Yes.',
    'Signs point to yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.',
    ' Cannot predict now.','Concentrate and ask again.',"Don't count on it.",'My reply is no.',
    'My sources say no.','Outlook not so good.','Very doubtful.']
    random_answer= random.choice(answers)
    print (random_answer)

print("Welcome to the magic 8 program!")
while(True):
    question = getQuestion()
    if(checkQuestion(question)):
        print("here's an answer: ")
        getanswers()


