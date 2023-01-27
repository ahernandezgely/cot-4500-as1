import decimal

# Question 1

str = "0100000001111110101110010000000000000000000000000000000000000000"

s = int(str[0])
s: float = decimal.Decimal((-1)**s)

c: float = 0
i = 1
bit: int =  0

while i < 12:
    bit = int(str[i])
    if bit > 0:
        c += decimal.Decimal(2**(11-i))
    i += 1

f: float = 0

while i < len(str):
    bit = int(str[i])
    if bit > 0:
        f += decimal.Decimal((1/2)**(i - 11))
    i +=1

val = s * (2 ** (c - 1023)) * (1 + f)

print(float(val))

# Question 2 & 3:

chopping = float(int((val * 10)/10))
rounding = decimal.Decimal((round(val)))

print("\r")
print(chopping)
print("\r")
print(float(rounding))

# Question 4:

absolute = abs(val - rounding)

relative = abs(absolute / val)

print("\r")
print(float(absolute))
print('{0:.31f}'.format(relative))

# Question 5:

n = (10 ** (4/3)) - 1
print("\r")
print(round(n))


# Question 6a:

#Bisection method:

def func(x):
    return (x * x * x) + (4 * x * x) - 10

tol: float = 0.0001
left: float = -4
right: float = 7

max = 50

i = 0

while abs(right - left) > tol and i < max:
    i+=1
    p = (left + right)/2
    
    
    if (func(left) < 0 and func(p) > 0) or (func(left) > 0 and func(p) < 0):
        right = p
    else:
        left = p

print("\r")
print(i)

# Question 6b:

# Newton-Raphson method

def firstDeriv(x):
    return (3 * x * x) + (8 * x)

prev = 7
tol: float = 0.0001
max = 50

i = 1

while i <= max:
    if firstDeriv(prev) != 0:
        next = prev - func(prev)/firstDeriv(prev)
        
        if abs(next - prev) < tol:
            print("\r")
            print(i)
            break
        
        i += 1
        prev = next
    else:
        print("\r")
        print("Deriv is 0")
        break

if i > max:
    print("\r")
    print("Deriv is 0")

