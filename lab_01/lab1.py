
array1, array2 = [], []

with open('/Users/macbookden/univer/backend/lab_01/input_1.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.split())) 
        if len(numbers) == 2:
            array1.append(numbers[0])
            array2.append(numbers[1])

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  
    return arr


sorted_array1 = selection_sort(array1)
sorted_array2 = selection_sort(array2)


all_list = [abs(a - b) for a, b in zip(sorted_array1, sorted_array2)]

total_sum = sum(all_list)  

print("Висновок:", total_sum)