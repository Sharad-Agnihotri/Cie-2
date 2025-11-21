import sys


if len(sys.argv) == 3:
    qty = int(sys.argv[1])
    price = float(sys.argv[2])
else:
    
    qty = 12
    price = 100

total_bill = qty * price
print("Total bill is:", total_bill)
