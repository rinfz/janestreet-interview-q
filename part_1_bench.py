from timeit import timeit
from part_1 import query, preprocess

def test_case(fn, facts, q):
    result = []
    for n in (1_000, 10_000, 100_000, 1_000_000):
        result.append(timeit(
            lambda: fn(facts, q),
            number=n,
        ))
    return result


facts_short_first = preprocess([
    ('m', 100, 'cm'),
    ('m', 3.28, 'ft'),
    ('ft', 12, 'in'),
    ('in', 2.54, 'cm'),
    ('hr', 60, 'min'),
    ('min', 60, 'sec'),
])

facts_short_last = preprocess([
    ('m', 3.28, 'ft'),
    ('ft', 12, 'in'),
    ('in', 2.54, 'cm'),
    ('hr', 60, 'min'),
    ('min', 60, 'sec'),
    ('m', 100, 'cm'),
])

facts_no_short = preprocess([
    ('m', 3.28, 'ft'),
    ('ft', 12, 'in'),
    ('in', 2.54, 'cm'),
    ('hr', 60, 'min'),
    ('min', 60, 'sec'),
])

q = (2, 'm', 'cm')

simple_short_first = test_case(query, facts_short_first, q)
simple_short_last = test_case(query, facts_short_last, q)
simple_no_short = test_case(query, facts_no_short, q)

# TODO: get some percentages from these stats
print(simple_short_first)
print(simple_short_last)
print(simple_no_short)
