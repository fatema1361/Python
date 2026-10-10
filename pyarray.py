numbers=[12,45,23,53,54,23,13,67,3]
print(numbers[::-1])
odds=[]
for num in numbers:
    if num%2==1:
        odds.append(num)
print(odds)