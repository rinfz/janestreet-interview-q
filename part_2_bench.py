from timeit import timeit
from part_2 import query as query_simple, preprocess
from part_2a import query as query_terminating

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

assert query_simple(facts_short_first, q) == query_terminating(facts_short_first, q)
assert query_simple(facts_short_last, q) == query_terminating(facts_short_last, q)
assert query_simple(facts_no_short, q) == query_terminating(facts_no_short, q)

simple_short_first = test_case(query_simple, facts_short_first, q)
simple_short_last = test_case(query_simple, facts_short_last, q)
simple_no_short = test_case(query_simple, facts_no_short, q)

term_short_first = test_case(query_terminating, facts_short_first, q)
term_short_last = test_case(query_terminating, facts_short_last, q)
term_no_short = test_case(query_terminating, facts_no_short, q)

# TODO: get some percentages from these stats
print(simple_short_first, term_short_first)
print(simple_short_last, term_short_last)
print(simple_no_short, term_no_short)
