a =[]
b=()
c = int(input("Enter the no of element : "))

for i in range (0,c):
  d = float(input("Enter the element : "))
  a.append(d)
print("The list is : ",a)

b = tuple(a)
print( "Tupple list is : " ,b )

sorted_1 = sorted(b)
d= tuple(sorted_1)
print( "Sorted list is : ",d)

'''
Enter the no of element : 5
Enter the element : 12.5
Enter the element : 16.7
Enter the element : 8.0
Enter the element : 9.7
Enter the element : 4.3
The list is :  [12.5, 16.7, 8.0, 9.7, 4.3]
Tupple list is :  (12.5, 16.7, 8.0, 9.7, 4.3)
Sorted list is :  (4.3, 8.0, 9.7, 12.5, 16.7)

'''

