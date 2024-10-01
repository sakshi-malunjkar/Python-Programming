Seconds = int(input("Enter Seconds: "))
print("Seconds : ",Seconds)
Hours = (Seconds//3600)
print("Hours  : ",Hours)
Ho_rs= (Seconds%3600)

Min = Ho_rs//60
print("Minutes : ",Min)
seconds=Ho_rs%60
print("Seconds: ",seconds)

'''
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B2_31/Sem 2$ python3 Assignment1.py
Enter Seconds: 3666
Seconds :  3666
Hours  :  1
Minutes :  1
Seconds:  6

'''

