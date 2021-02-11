import math
#print((108/79)-math.tan(108))
n = input()

if n == 1:
    x, y, z = input(), input(), input()
    print((17*y**4-y**7/13)/(y**3-54*y**4)-(20*z**3+95*x**8+11)/(math.tan(z)-51*y**8)+z**6-math.log(z,math.e))
elif n == 2:
    x = input()
    if x<72:
        print(47*(math.sin(x)-97*x**8)**3+54*x**5)
    elif x<92:
        print(x**5+35*x**6-94)
    elif x<165:
        print((x/79)-math.tan(x))
    elif x<249:
        print(75*x**3-math.tan(x))
    else:
        print(math.log(x**2+math.tan(x),math.e)-x**7+66)
elif n == 3:
    n, m = input(), input()
    s = 0
    for i in range(1, n+1, 1):
        for j in range(1, m+1, 1):
            s += (17*i**4-i**7/13)-18*(i**7+math.tan(j))
    print(s)
elif n == 4:
    def rec(n):
        if n == 0:
            return 3
        else:
            return (rec(n-1)/49)-(math.cos(rec(n-1)))
    n = input()
    print(rec(n))
