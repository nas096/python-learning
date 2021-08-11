def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError("Please enter a valid length")

    result = []
    for i in range(len(series)):
        slice = series[i:length+i]
        if len(slice) == length:
            result.append(slice)

    return result
