
print(2**3) # dấu ** là dấu mủ ^

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result # return giúp kết thúc functions
print(raise_to_power(3, 4))
# cách hoạt động: cho số vd như 4(range là 0,1,2,3) thì lặp lại số lần như vậy
