def quick_sort(values):
    if len(values) <= 1:
        return values.copy()
    pivot = values[len(values) // 2]
    smaller = [x for x in values if x < pivot]
    equal = [x for x in values if x == pivot]
    greater = [x for x in values if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(greater)
