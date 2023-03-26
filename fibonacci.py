
t = int(input("Enter Number of Terms to print: "))
n1 = 0
n2 = 1
for x in range(0,t):
    print(n1,end='  ') 
    n3 = n1 + n2
    n1 = n2
    n2 = n3
