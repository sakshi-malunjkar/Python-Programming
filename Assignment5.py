
a=[]
b=int(input("Enter the no of element : "))

for i in range(0,b):
 c = int(input("Enter the element : "))
 a.append(c)
print("List is : " ,a) 

print( "Sum is : ",sum(a))
print("Length is : ",len(a))
print("Maximum is : ",max(a))
print("Minimum is : ",min(a))
Avg=sum(a)/len(a)
print("Avg is : ",Avg)
print("Reverse list is : ", a[::-1])


'''
Enter the no of element : 5
Enter the element : 20
Enter the element : 10
Enter the element : 30
Enter the element : 40
Enter the element : 50
List is :  [20, 10, 30, 40, 50]
Sum is :  150
Length is :  5
Maximum is :  50
Minimum is :  10
Avg is :  30.0
Reverse list is :  [50, 40, 30, 10, 20]

'''
