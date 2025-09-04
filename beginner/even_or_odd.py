


def checkUserNumber():
    print('hello')
    userInput=int(input('INPUT A NUMBER'))
    if userInput<0:
        print('PUT A POSITIVE NUMBER')
    else:
        if userInput%2==0:
            print('THE NUMBER IS AN EVEN NUMBER')
        else:
            print('THIS NUMBER IS AN ODD NUMBER')
    
    

checkUserNumber()
    
