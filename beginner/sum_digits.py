
def sumDigits(numbers):
    sum=0
    chars=str(numbers)
    # print(chars)
    for char in chars:
        sum+=int(char)
    print(sum)

sumDigits(123)
        