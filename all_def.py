def even_odd():                   # Short example
    n = input("enter number:")
    n = int(n)
    if n % 2 ==0:
        print("n is even")
    else:
        print("n is odd")

even_odd()
even_odd()
even_odd()

n = input("enter you number:")     # Long example
n = int(n)

if n % 2 == 0:
    print("n - even")
else:
    print("n - odd")

n = input("enter you number:")
n = int(n)

if n % 2 == 0:
    print("n - even")
else:
    print("n - odd")

n = input("enter you number:")
n = int(n)

if n % 2 == 0:
    print("n - even")
else:
    print("n - odd")

# A lot more :
def f(x):
    return x+1

z = f(4)

if z == 5:
    print("z equal 5")
else:
    print("z is not equal 5")


def f():
    return 1+1

result = f()
print(result)


def f(x, y, z):
    return x+y+z

result = f(4,5,1)
print(result)

def f():
    z= 1+1
result = f()
print(result)

len('USA')

# all build in functions

age = input("Give your age:")
int_age = int(age)
if int_age < 21:
    print("You are awesome !")
else:
    print("You are old dude!")

# Many times def

def even_odd(x):
    if x % 2 ==0:
        print("even")
    else:
        print("odd")

result = even_odd(4)
print(result)
def f(x=2):
    return x**x
print(f())
print(f(10))

def add_it(x, y=10):
    return x+y
result = add_it(2)
print(result)



import math

#long of diaoganal 

l=4
w=10
d= math.sqrt(l**2 + w**2)

print(d)


a = 'qwertyuiopasdfghjklzxcvbnm'

print(*sorted(a))

