#AN INTERVIEW CHALLENGE
#FIZZ BUZ
#PRINT NUMBER 1-50 AND FOR EACH NUMBER DIVISIBLE BY 3->PRINT FIZZ
##AND NUMBER DIVISIBLE BY 5 ->PRINT BUZZ
#ELSE PRINT FIZZBUZZ

def printFizzbuzz():
    for i in range(50):
        if i%3==0:
            print('fizz')
        elif i%5==0:
            print('buzz')
        else:
            print('fizzbuzz')


printFizzbuzz()
        