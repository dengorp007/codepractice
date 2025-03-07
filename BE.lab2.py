def min_distance_sum(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

def is_safe_report(report):
    increasing = all(b > a and 1 <= b - a <= 3 for a, b in zip(report, report[1:]))
    decreasing = all(b < a and 1 <= a - b <= 3 for a, b in zip(report, report[1:]))
    return increasing or decreasing

def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe_report(report))

# Приклад використання
left = [3, 4, 2, 1, 3, 3]
right = [4, 3, 5, 3, 9, 3]
result = min_distance_sum(left, right)
print("Загальна відстань:", result)

reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

safe_count = count_safe_reports(reports)
print("Кількість безпечних звітів:", safe_count)
