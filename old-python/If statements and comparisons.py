
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # so sánh như vậy giúp đưa ra boolean và có thể so sánh với bất kì dữ liệu nào
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3
print(max_num(3,4,5))

#!= là dấu ko bằng
#== tương đương