from typing import List

test_list = [2,6,3,22,77,43,37,83,32,44,33,63,363,342,34526,3454,334,3,2,4,6,7,8,9]

def binary_search(search: int, input: List[int] = test_list) -> bool:
    sorted_input = sorted(input)
    if len(sorted_input) == 0: return False
    if len(sorted_input) == 1: return sorted_input[0] == search
    high = len(sorted_input)
    low = 0
    while high >= low:
        mid = low + (high-low) // 2
        select = sorted_input[mid]
        if select == search:
            return True 
        elif search < select:
            high = mid-1
        elif search > select:
            low = mid+1
    return False

def recursive_binary_search(l: int, h: int, search: int, input: List[int]) -> bool:
    if len(input) == 0: return False
    if h >= l:
        mid = l + (h-l) // 2
        select = input[mid]
        if search == select:
            return True
        if search < select:
            return recursive_binary_search(l, mid-1, search, input)
        if search > select:
            return recursive_binary_search(mid+1, h, search, input)
    return False


if __name__ == "__main__":
    assert binary_search(342) == True
    assert binary_search(42) == False
    assert binary_search(2,[]) == False
    assert binary_search(1,[0]) == False
    assert binary_search(1,[1]) == True
    assert recursive_binary_search(0, len(test_list), 342, sorted(test_list)) == True
    assert recursive_binary_search(0, len(test_list), 42, sorted(test_list)) == False
    assert recursive_binary_search(0, len([]), 2, []) == False
    print("\nSuccess")