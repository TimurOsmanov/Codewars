import itertools
import functools


def eval_prod_sum(lst, num_fact, num_add, max_val):
    arg = [num_fact, num_add, max_val]
    for e in lst:
        if isinstance(e, float) or isinstance(e, str):
            return "Error. Unexpected entries"
    for a in arg:
        if isinstance(a, float) or isinstance(a, str) or a <= 0:
            return "Error. Unexpected entries"
    products = list(x for x in itertools.combinations(lst, num_fact))
    sums = list(functools.reduce(lambda x, y: x * y, q) for q in products)
    united_sums_tuple = list(x for x in itertools.combinations(sums, num_add))
    united_sums = list(sum(s) for s in united_sums_tuple)
    below = equal = higher = 0
    for i in united_sums:
        if i < max_val:
            below += 1
        elif i == max_val:
            equal += 1
        else:
            higher += 1
    if num_fact > len(lst):
        return "Error. Number of factors too high"
    elif num_add > len(products):
        return "Error. Number of addens too high"
    else:
        return [{f"Below than {max_val}": below},
                {f"Equals to {max_val}": equal},
                {f"Higher than {max_val}": higher}]
