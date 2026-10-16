import pytest
from sorting.bubble_sort import bubble_sort
from sorting.quick_sort import quick_sort


@pytest.mark.parametrize('sort_function', [bubble_sort, quick_sort])
@pytest.mark.parametrize('values', [[], [1], [3, 1, 2], [5, -1, 5, 0], [1, 2, 3], [3, 2, 1]])
def test_sorting(sort_function, values):
    original = values.copy()
    assert sort_function(values) == sorted(values)
    assert values == original
