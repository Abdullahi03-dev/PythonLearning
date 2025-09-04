

def reverseInput():
    userInput=input('WRITE A STRING TO REVERSE->')
    if isinstance(userInput,str):
        userInput=userInput[::-1]
        print(userInput)
    else:
        print('PUT A VALID STRING')

reverseInput()