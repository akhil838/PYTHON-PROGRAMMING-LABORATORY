principal = int(input("Enter Principal Amount: "))
rate = int(input("Enter Rate of Interest: ")) / 100
time = int(input("Enter Time Period: "))
n = int(input("Enter Number of times the interest is compounded annually: "))
amount = principal*((1+ (rate/n))**(n*time))

print("Compound Interest is %.2f"%amount)
