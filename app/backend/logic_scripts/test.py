def compute_hamming_distance(code_1, code_2):
    distance = 0
    for index in range(len(code_1)):
        if code_1[index] != code_2[index]:
            distance += 1
    return distance

def espresso_reduction(on_set, off_set):
    visited = set()
    temp_on = []
    start = on_set
    for i, code_1 in enumerate(on_set):
        if i in visited:
            continue
        combined = False
        for j in range(i+1, len(on_set)):
            if j in visited:
                continue
            diff = compute_hamming_distance(code_1, on_set[j])
            if diff > 1:
                continue
            temp_expression = []
            for bit_index in range(0, len(code_1)):
                if code_1[bit_index] != on_set[j][bit_index]:
                    temp_expression.append(-1)
                else:
                    temp_expression.append(code_1[bit_index])
            visited.add(j)
            temp_expression = tuple(temp_expression)
            temp_on.append(temp_expression)
            combined = True
            break
        if not combined:
            temp_on.append(code_1)
    temp_on = tuple(temp_on)
    if temp_on != start:
        return espresso_reduction(temp_on, off_set)
    return on_set

def espresso(on_sets, off_sets):
    new_on_sets = []
    for on_set, off_set in zip(on_sets, off_sets):
        on_set = espresso_reduction(on_set, off_set)
        new_on_sets.append(on_set)
    return new_on_sets

print(espresso([((1,1,0),(1,1,1)), ((0,0,1),(0,1,0),(1,0,1),(1,1,0))], [((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1)),((0,0,0),(0,1,1),(1,0,0),(1,1,1))]))