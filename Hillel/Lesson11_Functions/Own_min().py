def own_min(iterable):
    min_value = iterable[0]

    for item in iterable[1:]:
        if item < min_value:
            min_value = item

    return min_value

numbers = [2,3,4]
result = own_min(numbers)
print(result)
