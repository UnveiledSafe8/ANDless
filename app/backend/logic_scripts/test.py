class ASTNode:
    def __init__(self, op, left=None, right=None, value=None):
        self.op = op
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        if self.op == "VAR":
            return self.value
        elif self.op == "NOT":
            return f"NOT {self.left}"
        return f"({self.left} {self.op} {self.right})"

def truthTable2Sets(table):
    on_sets = [[] for index in range(len(list(table.values())[0]))]
    off_sets = [[] for index in range(len(list(table.values())[0]))]
    for values, truths in table.items():
        for truth_index, truth in enumerate(truths):
            if truth == 0:
                off_sets[truth_index].append(values)
            elif truth == 1:
                on_sets[truth_index].append(values)
    for index in range(len(on_sets)):
        on_sets[index] = tuple(on_sets[index])
    for index in range(len(off_sets)):
        off_sets[index] = tuple(off_sets[index])
    
    on_sets = tuple(on_sets)
    off_sets = tuple(off_sets)

    return (on_sets, off_sets)
 
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

def espresso(sets):
    new_on_sets = []
    on_sets = sets[0]
    off_sets = sets[1]
    for index in range(len(on_sets)):
        on_set = espresso_reduction(on_sets[index], off_sets[index])
        new_on_sets.append(on_set)
    new_on_sets = tuple(new_on_sets)
    return new_on_sets

def cubes2rpn(cubes):
    equation = []
    total_cubes = 0
    for cube in cubes:
        productTerm = []
        total_vars = 0
        for index, input in enumerate(cube):
            if input == -1:
                continue
            productTerm.append("V" + str(index))
            total_vars += 1
            if input == 0:
                productTerm.append("NOT")
            if total_vars > 1:
                productTerm.append("AND")
        equation.extend(productTerm)
        total_cubes += 1
        if total_cubes > 1:
            equation.append("OR")
    return equation

def rpn2ast(equation):
    stack = []
    for ele in equation:
        if ele in ["AND", "OR", "XOR", "NAND", "NOR", "XNOR", "IMP", "BIMP"]:
            right = stack.pop()
            left = stack.pop()
            stack.append(ASTNode(ele, left, right))
        elif ele == "NOT":
            curr = stack.pop()
            stack.append(ASTNode(ele, curr))
        else:
            stack.append(ASTNode("VAR", value=ele))
    return stack.pop()






sets = truthTable2Sets({(0,0,0):(0,0), (0,0,1):(1,0), (0,1,0):(1,0), (0,1,1):(0,1), (1,0,0):(1,0), (1,0,1):(0,1), (1,1,0):(0,1), (1,1,1):(1,1)})

reduced_sets = espresso(sets)

for cubes in reduced_sets:
    print(rpn2ast(cubes2rpn(cubes)))