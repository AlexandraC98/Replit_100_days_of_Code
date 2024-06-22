bill=float(input("Bill: "))
tip=float(input("Tip percentage: "))
totalsum=bill+tip/100*bill
people=int(input("Number of people: "))
answer=round(totalsum/people,2)
print("Each has to pay: ",answer)
