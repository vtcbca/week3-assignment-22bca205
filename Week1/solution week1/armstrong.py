#4.Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.


def check_armstrong(n):
    cp=n
    sum=0
    while(n>0):
         d=n%10
         re=d*d*d
         sum=sum+re
         n=n//10
    if cp==sum:
        print('Entered number is armstrong number')
    else:
        print('Entered number is  no armstrong  number')
n=int(input("Enter any number:"))
check_armstrong(n)
