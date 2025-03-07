def min_distance_sum(left_list, right_list):
    
    left_list.sort()
    right_list.sort()
    
   
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    return total_distance

left = [3, 4, 2, 1, 3, 3]
right = [4, 3, 5, 3, 9, 3]

result = min_distance_sum(left, right)
print("Загальна відстань:", result)
