import operator
from decimal import Decimal
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

    # find viable paths
    best_path = sorted(
        (
            viable for n in facts
            if n[0] == src and (viable := inner(n)) is not None
        ),
        # invert all with not because False => 0 and 0 sorts before 1
        key=lambda x: (len(x), not all(isinstance(xx, int) for xx in x)),
    )
    print(best_path)

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


if __name__ == '__main__':
    facts = preprocess([
        ('m', Decimal('3.28'), 'ft'),
        ('ft', 12, 'in'),
        ('in', Decimal('2.54'), 'cm'),
        ('hr', 60, 'min'),
        ('min', 60, 'sec'),
        # example  (think of a real example?)
        ('m', 10, 'tmp1'),
        ('tmp1', 2, 'tmp2'),
        ('tmp2', 5, 'cm'),
    ])

    print(query(facts, (2, 'm', 'cm')))
