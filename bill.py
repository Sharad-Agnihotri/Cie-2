import sys
if len(sys.argv)>3:
    qty=sys.argv[1]
    price_per_item=sys.argv[2]
    print("Invalid parameters")
else:
    qty=2
    price_per_item=100
    total_bill=qty*price_per_item
    print("Total bill is:",total_bill)