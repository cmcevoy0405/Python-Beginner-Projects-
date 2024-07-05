def factorial(n):
    if n <= 1:
        return 1
    else:
       return n * factorial(n-1)

print(factorial(2))

def count_leaf_items(item_list):
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1
    return count

names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

print(count_leaf_items(names))

import statistics

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers)//2],
                numbers[-1]
            ]
        )
        item_less, item_pivot, item_more = (
        [n for n in numbers if n < pivot],
        [n for n in numbers if n == pivot],
        [n for n in numbers if n > pivot])

        return (quicksort(item_less) + item_pivot + quicksort(item_more))

import random

def get_random_numbers(length, minimum=1, maximum=100):
    numbers = []
    for _ in range(length):
        numbers.append(random.randint(minimum, maximum))

    return numbers

print(quicksort(get_random_numbers(30, 1, 100)))
