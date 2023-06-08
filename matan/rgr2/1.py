s = 0
for n in range(1,5):
    a = (-1)**(n-1)/(2**(6*n-5)*(6*n-5)*n)
    s+=a
    print(a)
print(s)