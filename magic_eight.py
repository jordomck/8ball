
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


print("Welcome to the magic 8 program!")
while(True):
    question = getQuestion()
    if(checkQuestion(question)):
        print("here's an answer: ")
        #print answer 
