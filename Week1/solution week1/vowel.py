#5.Write a python script to enter any string and count vowel.

def count_vowels(string):
    b=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i in vowels:
            b+=1
    print(f"Vowels In String Are {b}")
string=input("\n Enter the String :")
count_vowels(string)
