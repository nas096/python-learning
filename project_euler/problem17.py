from num2words import num2words
oneToThousandWords = [num2words(i).replace(
    " ", "").replace("-", "") for i in range(1, 1001)]


print(sum([len(j) for j in oneToThousandWords]))
