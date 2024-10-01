row = int(input("Ener No of Rows : "))

for i in range(0,row):

   for j in range(0,row-i):
       print("*",end=' ')
 
   print( )

'''
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B2_31/Sem 2$ python3 program22.py
Ener No of Rows : 5
* * * * * 
* * * * 
* * * 
* * 
* 
'''
