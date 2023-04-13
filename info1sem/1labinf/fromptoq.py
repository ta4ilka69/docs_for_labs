q, n = map(int,input().split())
s = ''
while n!=0:
    print(n//q,n%q)
    s=str(n%q)+s
    n = n//q
print(s)