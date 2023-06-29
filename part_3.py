def preprocess(facts):
    result = {}
    for from_, mul, to in facts:
        result[from_, to] = mul
    return result

def parse(facts):
    swap = True
    while swap:
        swap = False
        for b, e in [*facts.keys()]:
            ks = [n[1] for n in facts.keys() if n[0] == e]
            for k in ks:
                # nice thing here is direct/shorter relations will not be
                # overwritten
                if (b, k) not in facts:
                    swap = True
                    facts[b, k] = facts[b, e] * facts[e, k]
    return facts

def gen_query(facts0):
    facts = parse(facts0)

    # keep same arity for api
    def inner(_, q):
        qty, *rest = q
        key = tuple(rest)
        if key not in facts:
            return 'not convertible!'
        else:
            return qty * facts[key]

    return inner


def direct_query(facts, q):
    facts = parse(facts)
    qty, *rest = q
    key = tuple(rest)
    if key not in facts:
        return 'not convertible!'
    else:
        return qty * facts[key]


if __name__ == '__main__':
    facts = preprocess([
        ('m', 3.28, 'ft'),
        ('ft', 12, 'in'),
        ('in', 2.54, 'cm'),
        ('m', 100, 'cm'),
        ('hr', 60, 'min'),
        ('min', 60, 'sec'),
    ])

    q = (2, 'm', 'cm')
    iq = gen_query(facts.copy())
    dq = direct_query
    print(iq(0, q))
    print(dq(facts.copy(), q))
