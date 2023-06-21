import operator
from functools import reduce

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
    # we want to pick the most efficient relation if possible
    def inner(node, mul=None):
        if node not in facts:
            return
        if node[1] == target:
            # mul or [] here if src -> target is direct relation
            return (mul or []) + [facts[node]]
        keys = [k for k in facts if k[0] == node[1]]
        for k in keys:
            return inner(k, (mul or []) + [facts[node]])

    # TODO: we should terminate early if len(inner(n)) == 1
    # NOTE: that would be definition order dependent
    # NOTE: other things to consider might be int mul vs float mul (better convert)
    # NOTE: the multiplier closest to 1 (i.e. src and target are close in magnitude)
    # find viable paths
    best_path = sorted(
        (
            viable for n in facts
            if n[0] == src and (viable := inner(n)) is not None
        ),
        key=len,
    )

    if not best_path:
        return None
    return reduce(operator.mul, best_path[0])

def query(facts, q):
    qty, begin, end = q
    result = solve(facts, begin, end)
    if result is None:
        return 'not convertible!'
    else:
        return qty * result


facts = preprocess([
    ('m', 3.28, 'ft'),
    ('ft', 12, 'in'),
    ('in', 2.54, 'cm'),
    ('hr', 60, 'min'),
    ('min', 60, 'sec'),
    ('m', 100, 'cm'),
])

print(query(facts, (2, 'm', 'cm')))
