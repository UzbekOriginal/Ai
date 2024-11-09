arr1 = [1, 2, 2, 3, 4, 5, 5, 7, 6]

# Задача 1
max_element = max(arr1)
min_element = min(arr1)
print("Максимальный элемент:", max_element)
print("Минимальный элемент:", min_element)

# Задача 2
unique_arr = []
for item in arr1:
    if item not in unique_arr:
        unique_arr.append(item)

print("Массив без дубликатов (с сохранением порядка):", unique_arr)

# Задача 3
arr11 = [1, 2, 2, 3, 4]
arr22 = [5, 5, 7, 6]
combined_arr = arr11 + arr22
max_element_combined = max(combined_arr)

print("Максимальный элемент в объединённом массиве:", max_element_combined)
