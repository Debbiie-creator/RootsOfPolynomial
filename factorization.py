#Factoring
# 
#Function to prime factorize
def primeFac(n):
    f = []
    for i in range(1,int(abs(n)**(0.5))+1):
        if n%i==0:
            f.append(i)
            f.append(0-i)
            if i != (n//i):
                f.append(n//i)
                f.append(0-(n//i))
    return f

d = int(input("Enter degree of polynomial:"))
l =[]
for i in range(d+1):
    k = int(input(f"Enter the coefficient of x^{d-i}:"))
    l.append(k)

#Checkpoint   
#print(l)

#Function to calculate value of polynomial
def polynomial(x):
    s = 0
    for i in range(len(l)):
        s += l[i] * (x**(d-i))
    return s
#Checkpoint
#print(polynomial(2))
#Checking Integer Roots
roots = []
w = -1
while l[w] == 0:
    roots.append(0)
    w -= 1
p = primeFac(l[w])
for q in p:
    if polynomial(q) == 0:
        roots.append(q)
#Checkpoint
print("Integer roots:", roots)
#Checking Rational roots
rroots =[]
c = primeFac(l[0])
for b in p:
    for j in c:
        if  polynomial(b/j) == 0:
            rroots.append(b/j)
ret = set(rroots)
print("Rational roots:",list(ret))
