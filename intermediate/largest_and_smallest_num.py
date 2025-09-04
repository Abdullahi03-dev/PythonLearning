listNum=[9,2,3,4,5,6,7]
largest=listNum[0]
smallest=listNum[0]

for num in listNum:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num


print('LARGEST',largest)
print('SMALLEST',smallest)
        