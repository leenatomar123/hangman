year=int(input("enter the year"))
if year%4==0:
    if year%100!=0:
        if year%400==0:
            print("it is leap year")
        else:
            print("it is not year")    