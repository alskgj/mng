from random import shuffle, randint
import time


def insertion_sort(data):
    """Take next element and insert into sorted list at right position"""
    result = [data[0]]
    for new_element in data[1:]:

        if new_element > result[-1]:
            result = result + [new_element]
            continue

        for i, element in enumerate(result):
            if new_element < element:
                result = result[:i] + [new_element] + result[i:]
                break

    return result


def insertion_sort2(data):
    for i in range(1, len(data)):
        value = data[i]
        j = i
        while j > 0 and data[j-1] > value:
            data[j] = data[j-1]
            j -= 1
        data[j] = value
    return data


def selection_sort(data):
    """Find minimum and swap it with first unsorted"""

    for i in range(len(data)):
        min_index = data.index(min(data[i:]), i)
        data[i], data[min_index] = data[min_index], data[i]
    return data


def dummy_sort(data):
    for i in range(len(data)):
        current_min = data[i]
        current_idx = i
        for j in range(i+1,len(data)):
            if data[j] < current_min:
                current_min = data[j]
                current_idx = j
        data[i], data[current_idx] = data[current_idx], data[i]
    return data

def merge_sort(data):
    """ pop(0) is O(n), so this solution will run in O(n**2) instead of
    n*log(n)"""
    # base case
    if len(data) == 1:
        return data

    # split data into a left and right list
    mid = int(len(data)/2)
    left, right = merge_sort(data[:mid]), merge_sort(data[mid:])
    result = []

    # merge it
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # one of the lists is empty, just append rest of the other list
    result = result + left + right

    return result


def merge_sort2(data):
    """solution not using pop(0), since pop(0) is in O(n),
    doesn't really speed up anything in python since overhead from function call is much
    larger anyway..."""
    # base case
    if len(data) == 1:
        return data

    # split data into a left and right list
    mid = int(len(data)/2)
    left, right = merge_sort(data[:mid]), merge_sort(data[mid:])

    result = []
    # merge it
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # one of the lists is empty, just append rest of the other list
    result = result + left[i:] + right[j:]

    return result


def quick_sort(data):
    if not data:
        return []
    return quick_sort([e for e in data if e < data[0]]) + [data[0]]*data.count(data[0]) + quick_sort([e for e in data if e > data[0]])


def heap_sort(data):
    return data


def generate_testdata(n=100):
    return [randint(1, n) for _ in range(10)]

if __name__ == '__main__':
    test_data = generate_testdata()
    print("Test data:             %s" % sorted(test_data))
    shuffle(test_data)
    print("Insertion sort result: %s" % insertion_sort2(test_data))
    shuffle(test_data)
    print("Selection sort result: %s" % selection_sort(test_data))
    shuffle(test_data)
    print("Dummy sort result:     %s" % dummy_sort(test_data))
    shuffle(test_data)
    print("Quicksort result:      %s" % quick_sort(test_data))
    shuffle(test_data)
    print("Mergesort result:      %s" % merge_sort(test_data))

