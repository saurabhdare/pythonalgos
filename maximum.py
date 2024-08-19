mylist = [1, 5, 5, 5, 5, 1]
max = mylist[0]
index = 0

for i in range(1, len(mylist)):
    if mylist[i] > max:
        max = mylist[i]
        index = i
        print(index)

print(index)
