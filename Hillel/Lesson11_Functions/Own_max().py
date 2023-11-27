def own_max(iterable):
    max_value = iterable[0]

    for item in iterable[1:]:
        if item > max_value:
            max_value = item

    return max_value

numbers = [3,4,5]
print(result = own_max(numbers))
