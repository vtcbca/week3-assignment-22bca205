#2.Write a python script to enter any number and print the sum of its digit.

a=int(input("Enter any number:"))
sum=0
no=a
while(a!=0):
    sum=sum+a%10
    a=a//10
print("sum of digits of {} is {}".format(no,sum))
