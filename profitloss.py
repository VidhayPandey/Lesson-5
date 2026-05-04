cp=float(input("Enter a Cost Price:"))
sp=float(input("Enter a Selling Price:"))

if sp>cp:
    amount=sp-cp
    print(f"Profit is {amount}$ on the deal.") 
elif cp>sp:
    amount= cp-sp
    print(f"Loss is {amount}$ on the deal")
else:
    print("no profit no loss.")

