#6.Write a python script to enter any string and print only part of string. Take input of start character and end character from user.

def substring(string):
    startindex=int(input("\n\nEnter Starting Index For Making Substring :"))
    endindex=int(input("\nEnter ending Index For Making Substring :"))
    print(f"\n\tSubstring Which Starts From {startindex} Index And End At {endindex} Index Is Below :\n\t ---> {string[startindex-1:endindex+1]}")
string=input("\n Enter String :")
substring(string)
