import random


def arr(length: int, value=0) -> list[int]:
    return [value for i in range(length)]


def random_arr(length, min_value=0, max_value=9):
    return [random.randint(min_value, max_value) for _ in range(length)]


def reverse(arr: list[int]):
    return arr[::-1]


def shift_left(arr, fill=0, length=1):
    return arr[length:] + [fill for i in range(length)]


def shift_right(arr, fill=0, length=1):
    return [fill for i in range(length)] + arr[:-length]


def replace_value(arr, src, dst):
    return [dst if x == src else x for x in arr]


def crop_nonzero(arr):
    idx = [i for i, x in enumerate(arr) if x != 0]

    if not idx:
        return []

    return arr[min(idx) : max(idx) + 1]


def repeat(arr, n):
    return arr * n


def repeat_each(arr, n):
    result = []
    for x in arr:
        result.extend([x] * n)
    return result


def mirror(arr):
    return arr + arr[::-1]


# def add_constant(arr, c=2):
#     return [x + c for x in arr]


def add_1(arr, c=1):
    return [x + c for x in arr]


def add_2(arr, c=2):
    return [x + c for x in arr]


def add_3(arr, c=3):
    return [x + c for x in arr]


def randint(start, stop):
    return random.randint(start, stop)


def rotate_left(arr, k=1):
    k = k % len(arr)
    return arr[k:] + arr[:k]


def rotate_right(arr, k=1):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]


# def swap(arr, i=0, j=-1):
#     arr = arr.copy()
#     arr[i], arr[j] = arr[j], arr[i]
#     return arr


def swap_first_last(arr, i=0, j=-1):
    arr = arr.copy()
    arr[i], arr[j] = arr[j], arr[i]
    return arr


# def prepend_zeros(arr: list[int], length=1):
#     return [0 for i in range(length)] + arr


# def append_zeros(arr: list[int], length=1):
#     return arr + [0 for i in range(length)]


def prepend_zero(arr: list[int], length=1):
    return [0 for i in range(length)] + arr


def append_zero(arr: list[int], length=1):
    return arr + [0 for i in range(length)]


def pop_left(arr: list[int], length=1):
    return arr[length:]


def pop_right(arr: list[int], length=1):
    return arr[:-length]


def insert(arr: list[int], i: int, value: int):
    arr = arr.copy()
    arr.insert(i, value)
    return arr


def delete(arr: list[int], i: int):
    return arr[:i] + arr[i + 1 :]


def get_at(arr: list[int], i: int):
    return arr[i]


def subtract_constant(arr, c):
    return [x - c for x in arr]


# def multiply_constant(arr, c=2):
#     return [x * c for x in arr]


def multiply_2(arr, c=2):
    return [x * c for x in arr]


def multiply_3(arr, c=3):
    return [x * c for x in arr]


# def modulo(arr, m=3):
#     return [x % m for x in arr]


def mod_2(arr, m=2):
    return [x % m for x in arr]


def mod_3(arr, m=3):
    return [x % m for x in arr]


def negate(arr):
    return [-x for x in arr]


def abs_values(arr):
    return [abs(x) for x in arr]


def sort_ascending(arr):
    return sorted(arr)


def sort_descending(arr):
    return sorted(arr, reverse=True)


# def differences(arr):
#     return [arr[i] - arr[i + 1] for i in range(len(arr) - 1)]


def subtract_next(arr):
    return [arr[i] - arr[i + 1] for i in range(len(arr) - 1)]


# def pairwise_sum(arr):
#     return [arr[i] + arr[i + 1] for i in range(len(arr) - 1)]


def adjacent_sum(arr):
    return [arr[i] + arr[i + 1] for i in range(len(arr) - 1)]


def take_even_positions(arr):
    return arr[::2]


def take_odd_positions(arr):
    return arr[1::2]
