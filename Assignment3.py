row = int(input("Ener No of Rows : "))
num = 1
for i in range(0,row):

   for j in range(0,i+1):
       print(num,end=' ')
       num=num+1
 
   print( )

'''
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B2_31/Sem 2$ python3 Assignment3.py
Ener No of Rows : 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''
