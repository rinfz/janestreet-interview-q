from timeit import timeit
from part_1_bench import test_case, avg
from part_2a import query as query_terminating, preprocess
from part_3 import gen_query


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

query_pf_sf = gen_query(facts_short_first.copy())
query_pf_sl = gen_query(facts_short_last.copy())
query_pf_ns = gen_query(facts_no_short.copy())

assert query_pf_sf(facts_short_first, q) == query_terminating(facts_short_first, q)
assert query_pf_sl(facts_short_last, q) == query_terminating(facts_short_last, q)
# oof
assert round(query_pf_ns(facts_no_short, q), 4) == query_terminating(facts_no_short, q)

pf_short_first = test_case(query_pf_sf, facts_short_first, q)
pf_short_last = test_case(query_pf_sl, facts_short_last, q)
pf_no_short = test_case(query_pf_ns, facts_no_short, q)

print("Cached")
print(avg(pf_short_first))
print(avg(pf_short_last))
print(avg(pf_no_short))
