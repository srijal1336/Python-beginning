"""name="srijal"
age=18
salary=1000.99

age2=age

print("My name is :", name)
print( "My age is :", age2)
print("My salary is :", salary)

print(type(name))
print(type(age))
print(type(salary)) """


#printing the sum of two number

"""a=5
b=9
sum=a+b
print(sum)"""

#Expression execution
"""A,B=2,3
Txt="@"
print(A*Txt*B)"""

"""A,B="2",3
Txt="@"
print((A+Txt)*B)"""

#Arithmetic expression with integer and float will be the result in float
"""A,B=1.5,5
C=A*B
print(C)"""

#Result of division operator with two integers will be float
'''A,B=1,2
C=A/B
print(C)

#Integer division with float and int will give int displayed as float
A,B=1.5,3
C=A//B
print(C)

#Result of(A//B)is same as floor(A/B)
A,B=-12,5
C=A//B
print(C)'''

#Remainder is negative when denominator is negative
"""A,B=-5,2
C=A%B
print(C)

A,B=5,-2
C= A%B
print(C)"""

#Taking input from user and printing it

'''name= input("name:")
age= int(input("age: "))
salary= float(input("salary: "))

print("My name is",name ,"and I am ",age, "years old and my salary is",salary )'''

#conditional statement
"""age=int(input("age: "))
if(age>=18):
    print("you are eligible for voting")
elif(age<18):
    print("you are not eligible for voting")"""
 
#traffic light system

'''light= input("light = ")
if(light=="red"):
    print("Stop")
elif(light=="orange"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")'''

#to see the grade of student

'''marks=float(input("marks: "))
if(marks>=90):
    print("you have secured grade A+")
elif(marks>=80 and marks<90):
    print("You have secured grade A")
elif(marks>=70 and marks<80):
    print("you have secured B+")
else:
    print("you are fail")'''


#ternary operator

'''food= input("food= ")
eat= "yes" if food== "cake" else "no"
print(eat)'''

'''food= input ("food:")
print("sweet") if food == "cake" or food=="jalebi" else print("not sweet")'''

#clever if atatement

'''age= int(input("age: "))
vote=("no", "yes") [age>18]
print(vote)'''

'''sal= float(input("salary:"))
tax= sal*(0.1,0.2) [sal>=50000]
print("the tax amount is:",tax)'''

#to calculate simple intrest
'''p= float(input("p : "))
t= float(input("t :"))
r= float(input("r :"))
 
si= (p*t*r)/100
print("the simple intrest of the given value is:",si)'''

'''a=10
b=90

print("Or operator:" , (a == b) or (a>b))'''

#type conversion

'''a= 2
b= 9.00
print(a+b)'''

#type casting
'''a=3.14
a= str("a")
print(type(a))'''

#input
'''int="3"
val= input("enter some value : ")
print(type(val),val)'''

'''name= input("enter your name:")
age= int(input("enter your age: "))
marks= float(input("enter your marks:"))

print("welcome", name)
print("age= ", age)
print("marks= ",marks)'''

#practice question

'''a=float(input("a= "))
b=float(input("b= "))
 
sum= a+b #sum of two numbers

print("the sum of the two number is= ", sum)'''

'''a=int(input("a= "))
area= a**2
print("the area of the square is: ", area)'''

'''a=float(input("a= "))
b=float(input("b= "))

average=(a+b)/2 #average

print("the average of the number is :", average)'''

'''a= int(input("a= "))
b= int(input("b= "))

print(a>=b)'''

 



