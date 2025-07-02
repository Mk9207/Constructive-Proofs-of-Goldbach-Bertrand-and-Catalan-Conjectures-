def generate_A_type_candidates(limit):
    return sorted(set(x for n in range(1, limit//6 + 2) for x in (6*n - 1, 6*n + 1) if x <= limit))

def generate_composite_exclusions(limit):
    base = generate_A_type_candidates(limit)
    return set(p*q for i, p in enumerate(base) for q in base[i:] if p*q <= limit)

def construct_primes(limit):
    A = set(generate_A_type_candidates(limit))
    R = generate_composite_exclusions(limit)
    result = sorted(A - R)
    if limit >= 2: result = [2] + result
    if limit >= 3 and 3 not in result: result = [2, 3] + [p for p in result if p != 2]
    return result
