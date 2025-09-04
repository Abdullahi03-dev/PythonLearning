

def count_vowels(text):
    vowels=['a','e','i','o','u']
    count=0
    
    for char in text:
        if char in vowels:
            count+=1
    print(count)
    
    
count_vowels('book')
    