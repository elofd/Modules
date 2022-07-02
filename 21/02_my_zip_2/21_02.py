def winrar(item1, item2):
    minlen = min(len(item1), len(item2))
    new_list = [(item1[i], item2[i]) for i in range(minlen)]
    return new_list
