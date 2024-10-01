Student1 = int(input("Enter Marks of Student1 : "))
print("Marks of Student1 is : " ,Student1)
Student2 = int(input("Enter Marks of Student2  : "))
print("Marks of Student2 is : ",Student2) 
Student3 = int(input("Enter Marks of Student3 : "))
print("Marks of Student3 is : " ,Student3)

a = ((Student1+Student2+Student3)/3)

if a>=90 and a<100 :
   print("Grade is : O")
elif a>=80 and a<90:
    print("Grade is : A")
elif a>=70 and a<80:
    print("Grade is : B")
elif a>=60 and a<70 :
    print("Grade is : C")
elif a>=50 and a<60 :
    print("Grade is : D")
elif a<=40 :
    print("Grade is : F")
else :
     print("Fail")
     
'''
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B2_31/Sem 2$ python3 Assignment2.py
Enter Marks of Student1 : 95
Marks of Student1 is :  95
Enter Marks of Student2  : 90
Marks of Student2 is :  90
Enter Marks of Student3 : 90
Marks of Student3 is :  90
Grade is : O

'''
