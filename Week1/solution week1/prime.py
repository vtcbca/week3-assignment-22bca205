#1.Write a python script to enter any number and check its prime or not.

def check_prime(no):
    for i in range(2,no,no):
        if no%i==0:
            print(f'{no} is  not prime number')
            break
        else:
            print(f'{no}is prime number')
no=int(input("Enter any number:"))
check_prime(no)
