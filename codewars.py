
t = "2\n10\n1000" 
t = t.split("\n")

t = [int(i) for i in t]


for j in range(1, t[0] + 1):

    multiple = [i for i in range(t[j]) if i%3 == 0 or i%5 == 0]
    print(sum(multiple))



