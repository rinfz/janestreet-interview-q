from timeit import timeit
from part_1 import query, preprocess

def test_case(fn, facts, q):
    result = []
    for n in (1_000, 10_000, 100_000, 1_000_000):
        result.append(1e6 * (timeit(
            lambda: fn(facts, q),
            number=n,
        ) / n))
    return result


def avg(xs):
    return sum(xs) / len(xs)


if __name__ == '__main__':
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

    print(avg(simple_short_first))
    print(avg(simple_short_last))
    print(avg(simple_no_short))
