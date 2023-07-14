#3.Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.

def check_palindrome(n):
    cp=n
    re=0
    if n:
        while(n>0):
            d=n%10
            re=re*10+d
            n=n//10
        print(f'reverse number{re}')
        if cp==re:
            print('Entered number is palindrome number')
        else:
            print('Entered number is  no palindrome  number')
    else:
        print('Entered number is  no integer number')
n=int(input("Enter any number:"))
check_palindrome(n)
