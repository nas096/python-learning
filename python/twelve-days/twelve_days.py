def recite(start_verse, end_verse):
    days = ['first',
            'second',
            'third',
            'fourth',
            'fifth',
            'sixth',
            'seventh',
            'eighth',
            'ninth',
            'tenth',
            'eleventh',
            'twelfth']

    gifts = ['a Partridge in a Pear Tree.',
             'two Turtle Doves, ',
             'three French Hens, ',
             'four Calling Birds, ',
             'five Gold Rings, ',
             'six Geese-a-Laying, ',
             'seven Swans-a-Swimming, ',
             'eight Maids-a-Milking, ',
             'nine Ladies Dancing, ',
             'ten Lords-a-Leaping, ',
             'eleven Pipers Piping, ',
             'twelve Drummers Drumming, ']

    return_versed = []
    for i in range(start_verse-1, end_verse):
        song = f"On the {days[i]} day of Christmas my true love gave to me: "

        if i == 0:
            song += gifts[0]

        else:
            for x in range(i, 0, -1):
                song += gifts[x]

            song += "and " + gifts[0]

        return_versed.append(song)

    return return_versed

# %%
