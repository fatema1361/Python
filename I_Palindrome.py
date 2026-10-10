N=input().strip()
reverse=N[::-1].lstrip('0')
print(reverse)
if N==reverse:
    print("YES")
else:
    print("NO")
