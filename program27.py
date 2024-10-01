string = input("Enter the String : ")

if(len(string)<3) :
  print("Enter the valid string")
  
else :
   print(string[0:2] + string[-2:])
   
   
'''
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B2_31/Sem 2$ python3 program27.py
Enter the String : python
pyon

pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B2_31/Sem 2$ python3 program27.py
Enter the String : py
Enter the valid string

'''
