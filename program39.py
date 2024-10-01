a=[] 
e=()
b = int(input("Enter the no of element : "))

for i in range (0,b):
  c=int(input("Enter elements : "))
  a.append(c)
print(a)
e=tuple(a[0:5]+[20,25,30]+a[0:5])
print(e)


'''

Enter the no of element : 5
Enter elements : 4
Enter elements : 5
Enter elements : 8
Enter elements : 7
Enter elements : 6
[4, 5, 8, 7, 6]
(4, 5, 8, 7, 6, 20, 25, 30, 4, 5, 8, 7, 6)

'''
