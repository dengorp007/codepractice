with open("/Users/macbookden/univer/backend/lab_06/input_6.txt", "r") as file:
    lines = [line.split() for line in file]


points = {'X': 1, 'Y': 2, 'Z': 3}


score_map = {
    ('A', 'X'): 3, ('B', 'Y'): 3, ('C', 'Z'): 3,  
    ('A', 'Y'): 6, ('B', 'Z'): 6, ('C', 'X'): 6,  
    ('A', 'Z'): 0, ('B', 'X'): 0, ('C', 'Y'): 0   
}

total_score = sum(score_map.get((opp, my), 0) + points[my] for opp, my in lines)

print("Підсумковий рахунок за всі раунди:", total_score)
