price=int(input("enter the price"))
if price>100000:
    print(15%100*price)
elif price>50000 and price<=100000:
    print(10%100*price)
else:
    print(5%1000*price)        