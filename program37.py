list=[]
list2=[]
list3=[]

n=int(input("Enter no of elements: "))
for i in range(0,n):
    b =int(input("Enter Element :"))
    list.append(b)
print("list:",list)
for j in list:
 if j%2==0:
   list2.append(j)
 else:
   list3.append(j)

print("Even numbers are : ",list2)
print("Odd numbers are : ", list3)

'''
Enter no of elements: 7
Enter Element :2
Enter Element :4
Enter Element :1
Enter Element :5
Enter Element :8
Enter Element :9
Enter Element :3
list: [2, 4, 1, 5, 8, 9, 3]
Even numbers are :  [2, 4, 8]
Odd numbers are :  [1, 5, 9, 3]

'''
     
