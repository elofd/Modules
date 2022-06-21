def slicer(mes, sym):
    index_count = []
    for index, num in enumerate(mes):
        if num == sym:
            index_count.append(index)
    if len(index_count) > 1:
        return mes[index_count[0]:index_count[-1]]
    elif len(index_count) == 1:
        return mes[index_count[0]:]
    return ()
