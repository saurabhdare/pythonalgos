my_array = [7, 12, 9, 3, 11]

# sort the array using Bubble Sort
n = len(my_array)

for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

print("Sorted array: ", my_array)
