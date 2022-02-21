def rearrange(array):
    if not array:
        return array
    first, *others = array
    if first % 2 == 0:
        return [first] + rearrange(others)
    return rearrange(others) + [first]


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rearrange(arr))
