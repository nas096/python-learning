'''
number_of_cats = 100
cats_with_hats = []
number_of_laps = 100

for lap in range(1, number_of_laps + 1):
    for cat in range(1, number_of_cats + 1):
        
        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)
print(cats_with_hats)
'''

theCats = {}

for i in range(1, 101):
    theCats[i] = False

for i in range(1, 101):
    for cats, hats in theCats.items():
        if cats % i == 0:
            if theCats[i]:
                theCats[i] = False
            else:
                theCats[i] = True

for cats, hats in theCats.items():
    if theCats[cats]:
        print(f"Cat {cats} has a hat")
    else:
        print(f"Cat {cats} is hatless")