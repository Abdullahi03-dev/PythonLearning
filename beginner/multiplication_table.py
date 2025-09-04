#input a number and a it print its table up to 12


def multiply(num):
    if isinstance(num,int):
        for i in range(13):
            print(i*num)
    else:
        print('PUT A VALID NUMBER')
        
        


multiply(2)