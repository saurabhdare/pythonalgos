my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

# solution 1
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j

    min_value = my_array[min_index]
    
    k = min_index
    # shifting values
    while k > i:
        my_array[k] = my_array[k - 1]
        k -= 1
    my_array[i] = min_value

print("Sorted array: ", my_array)

# solution 2
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index],my_array[i]

print("Sorted array: ", my_array)
