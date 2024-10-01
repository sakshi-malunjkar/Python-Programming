Price = input("Enter total price ")
print("Total price is ",Price)
Discount = input("Enter percentage of discount")
print("Percentage of Discount is ",Discount)
Discount_p = (float(Price)*float(Discount))/100
print("Toat Discount is ",Discount_p)
Amount = float(Price)-float(Discount_p)
print("Amount to be paid is ",Amount)

'''
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B2_31/Sem 2$ python3 program9.py
Enter total price 10000
Total price is  10000
Enter percentage of discount10
Percentage of Discount is  10
Toat Discount is  1000.0
Amount to be paid is  9000.0
'''
