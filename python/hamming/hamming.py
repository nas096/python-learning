def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("2 strands didn't have the same amount of DNA")

    return sum([dnaA != dnaB for dnaA, dnaB in zip(strand_a, strand_b)])
