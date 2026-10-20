t = int(input())

for i in range(t):
    s = input()
    a = str((len(s)-2))
    if len(s)>10:
        print(s[0] + a + s[-1:])
    else:
        print(s)