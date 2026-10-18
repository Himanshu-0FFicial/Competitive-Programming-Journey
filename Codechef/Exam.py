t = int(input())

for i in range(t):
    x,y,z = map(int, input().split())
    if (x*y)/2 < float(z):
        print("YES")
    else:
        print("NO")