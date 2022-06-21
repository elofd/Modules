def tpl_sort(numbers):
    for x in numbers:
        if type(x) != int:
            return numbers
    return sorted(numbers)
