def my_sum(*args):
    summa = 0
    for i in args:
        if isinstance(i, list):
            for value in i:
                if isinstance(value, list):
                    summa += my_sum(value)
                else:
                    summa += value
        else:
            summa += i
    return summa
