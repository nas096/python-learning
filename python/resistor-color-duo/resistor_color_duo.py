def value(colors):
    colorCode = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

    theCode = [str(colorCode[color]) for color in colors]

    theCode = "".join(theCode)

    return int(theCode)
