
# Problem:

# Given a smaller string s and a bigger string b, design an algorithm to find all permutations
# of the shorter string within the longer one. Print the location of each permutation.

def locate_all_permutations(s: str, b: str):
    start_value = 1
    s_values = {}
    sum_s = 0
    for item in s:
        if item not in s_values:
            s_values[item] = pow(2, start_value)
            start_value += 1

        value = s_values[item]
        sum_s += value

    locations = []
    sum_b = 0
    for idx in range(len(b)):
        item = b[idx]
        value = s_values.get(item, 999)

        if idx < len(s) - 1:
            sum_b = sum_b + value
        else:
            start = idx + 1 - len(s)
            sum_b = sum_b + value
            if sum_b == sum_s:
                locations.append((start, idx))

            first_value = s_values.get(b[start], 999)
            sum_b = sum_b - first_value

    return locations
