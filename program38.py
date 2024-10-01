a =[]
b=()
c = int(input("Enter the no of element : "))

for i in range (0,c):
  d = int(input("Enter the element : "))
  a.append(d)
print("The list is : ",a)

b = tuple(a)
print( "Tupple list is : " ,b )

sorted_1 = sorted(b)
d= tuple(sorted_1)
print( "Sorted list is : ",d)

'''
Enter the no of element : 5
Enter the element : 8
Enter the element : 5
Enter the element : 4
Enter the element : 9
Enter the element : 7
The list is :  [8, 5, 4, 9, 7]
Tupple list is :  (8, 5, 4, 9, 7)
Sorted list is :  (4, 5, 7, 8, 9)

'''
