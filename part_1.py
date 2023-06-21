# facts: List[Tuple[str, float, str]]
#   e.g. ('m', 3.28, 'ft')
# query: Tuple[float, str, str]
#   e.g. (2, 'm', 'in')

def preprocess(facts):
    result = {}
    for from_, mul, to in facts:
        result[from_, to] = mul
    return result

def solve(facts, src, target):
    def inner(node, mul):
        if node not in facts:
            return
        if node[1] == target:
            return mul * facts[node]
        keys = [k for k in facts if k[0] == node[1]]
        for k in keys:
            return inner(k, mul * facts[node])

    # find viable paths
    nodes = [n for n in facts if n[0] == src]
    for n in nodes:
        if (result := inner(n, 1)) is not None:
            return result
    return

def query(facts, q):
    qty, begin, end = q
    result = solve(facts, begin, end)
    if result is None:
        return 'not convertible!'
    else:
        return qty * result


facts = preprocess([
    ('m', 100, 'cm'), # move this to get different results
    ('m', 3.28, 'ft'),
    ('ft', 12, 'in'),
    ('in', 2.54, 'cm'),
    ('hr', 60, 'min'),
    ('min', 60, 'sec'),
])

print(query(facts, (2, 'm', 'cm')))
