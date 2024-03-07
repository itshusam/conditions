n1 = input("please enter the first number")
n2 = input("please enter the 2nd number")
n3 = input("please enter the 3rd number")

#1
if n1 > n2 and n1 > n3 :
    print ("the largest number is "+n1)
elif n2 > n1 and n2 > n3 :
    print ("the largest number is "+n2)
elif n3 > n1 and n3 > n2 :
    print("the largest number is "+n3)

#2
if n1 < n2 and n1 < n3 :
    print ("the smallest number is "+n1)
elif n2 < n1 and n2 < n3 :
    print ("the smallest number is "+n2)
elif n3 < n1 and n3 < n2 :
    print("the smallest number is "+n3)

#3
if n1 == n2 == n3 :
    print("all numbers are equal")
elif n1 == n2 and n1 > n3 :
    print("two numbers are the largest and its"+n1)
elif n1 == n3 and n1 > n2 :
    print("two numbers are the largest and its"+n1)
elif n3 == n2 and n3 > n1 :
    print("two numbers are the largest and its"+n3)