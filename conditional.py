#conditional statement if-elif-else
#light ="red"
#if(light == "green"):
 #   print("go")
#elif(light == "yellow"):
#    print("waait")
#else:
#    print("stop")

#STUDENT MARKS ANALYSIS
marks=float(input("enter marks"))
if(marks>=90):
    if(marks>=95):#nested if 
        print("grade a+")
    else:
        print("grade a")
elif(marks>=80):
    print("grade b")
elif(marks>=40):
    print("grade c")
else:
    print("fail")

    #to check number is even or odd
num=float(input("enter the number"))
if(num%2 == 0):
    if(num == 0):
        print("neither odd nor even")
    else:
        print("even")
else:
    print("odd") 

    #to check largest of three number
a=int(input("Enter first number"))
b=int(input ("enter second    number"))
c=int(input("enter third number"))
if(a == b or a == c or b == c):
     print( "same number entered ")
elif(a>b and a>c):
     print("a is greatest")
elif(b>c):
    print("b is greatest")
else:
    print("c is greatest")
    
