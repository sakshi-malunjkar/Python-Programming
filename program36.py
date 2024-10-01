a = [10,20,30,40,50]
key = 50
n = 5
count=0
for i in range(0,n) :

  if (a[i]==key) :
     print("The index of element is : ",i)
     count=count+1
     break
if (count==0):
    print("Element not found")
    
    
'''
The index of element is :  4

'''
