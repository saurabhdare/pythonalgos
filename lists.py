squares = [value ** 2 for value in range(1, 11)]

million = [i for i in range(1, 1000001)]
print(sum(million))

if million:
    print("It has some elements")
else:
    print("List is empty")
