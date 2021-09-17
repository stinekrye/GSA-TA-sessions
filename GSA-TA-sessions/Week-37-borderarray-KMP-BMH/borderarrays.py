#Implement a border array

def borderarray(x):
    ba = list([0] * len(x))
    for i in range(1,len(x)):
        b = ba[i-1]
        while x[b] != x[i] and b > 0: # We try to extend the different borders, by looking back through B to get the value at x[b] we can compare to x[i]. This is how we check if we can extend the border
            b -= 1
        if x[b] == x[i]:
            ba[i] = b + 1

    return ba

### Not done ###
def reverseborderarray(x):
    r = list([0]*len(x))
    for i in range(len(x)-2,-1,-1):
        ra = r[i-1]
        n = x[ra]
        m = x[i]
        while n != m and ra <= len(x)-1:
            ra +=1
            n = x[ra]
            m = x[i]
        if n == m:
            r[i] = len(x) - ra

    return r


x = "bacba"
y = "abcab"
re = reverseborderarray(x)
#ba = borderarray(y)
print(re)

# minus + terminates to fast

for i in range(len(x)-2,-1,-1):
    print(i)