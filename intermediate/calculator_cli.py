print('WELCOME TO CALCULATOR CLI')
#A SIMPLE CLI CALCULATOR





while True:
    input1=float(input('WRITE YOUR FIRST NUMBER->'))
    operation=input('WRITE A OPERATION SIGN TO USE->  +,-,*,/ ')
    input2=float(input('WRITE YOUR SECOND NUMBER->'))


    if operation=='+':
        result=input1+input2
    elif operation=='-':
        result=input1-input2
    elif operation=='*':
        result=input1*input2
    elif operation=='/':
        if input2!=0:
            result=input1/input2
        else:
            result='ERROR DIVISION BY ZERO'
    else:
        result='INVALID OPERATION WRITE A PROPER SIGN'
        
        

    print('RESULT->',result)