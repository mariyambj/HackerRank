def serviceLane(n, cases, width):
    results = []
    for case in cases:
        start, end = case
        min_width = min(width[start:end+1])
        results.append(min_width)
    return results
n = 8
width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
print(serviceLane(n, cases, width))

