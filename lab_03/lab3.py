
def calculate_sum(text_lines):
    total_sum = 0  
    
    for line in text_lines:
        digits = [char for char in line if char.isdigit()]  
        
        if digits:
            calibration_value = int(digits[0] + digits[-1])  
            total_sum += calibration_value
    
    return total_sum


with open('/Users/macbookden/univer/backend/lab_03/input_3.txt', 'r') as file:
    input_lines = file.readlines()


print(calculate_sum(input_lines))
