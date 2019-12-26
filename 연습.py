num = ""
for i in range(10):
    if i <= 5 and (i % 2)==0:
        continue
    elif i is 7 or i is 10:
        continue
    else:
        num = str(i) + num

print(num)
