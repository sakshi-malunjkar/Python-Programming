Salary = input("Enter Your Salary ")
print("Salary is ",Salary)
HRA = float(10)*float(Salary)/100
TA = float(5)*float(Salary)/100
Total_S = float(HRA)+float(TA)+float(Salary)
print("Total Salary is ",Total_S)
TAX = float(2)*float(Total_S)/100
Net_Salary = float(Total_S)-float(TAX)
print("Net Salary is ",Net_Salary) 
'''
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B2_31/Sem 2$ python3 program10.py
Enter Your Salary 10000
Salary is  10000
Total Salary is  11500.0
Net Salary is  11270.0
'''
