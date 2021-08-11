def color_code(color):
    colorDict = {}
    for index, col in enumerate(colors()):
        colorDict[col] = index

    return colorDict[color]


def colors():
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
