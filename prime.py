
m,n = input("Enter The Range to Print the prime numbers inbetween them (m, n): ").split()
y = 2
for x in range(int(m),int(n)+1):
    for y in range(2,x+1):
        if x%y == 0:
            break
    if x == y:
        print(x, end='  ')
