


userInput=input('TYPE A WORD->')
palindrome=userInput[::-1]
if userInput==palindrome:
    print(True,'IT IS A PALINDROME')
else:
    print(False,'IT IS A NOT A PALINDROME')