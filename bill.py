import sys
if len(sys.argv)>3:
    qty=sys.argv[1]
    price=sys.argv[2]
    print("Invalid parameters")
else:
    qty=12
    price=100
total_bill=qty*price
print("Total bill is:",total_bill)