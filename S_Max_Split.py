s=input()
count =0
temp=""
sub=[]

for ch in s:
    temp+=ch

    if ch=='L':
        count+=1
    else:
        count-=1
    if count==0:
        sub.append(temp)
        temp=""
print(len(sub))
for x in sub:
    print(x)


