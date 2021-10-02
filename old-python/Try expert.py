# nếu như user viết sai thì sẽ in ra invald input(ví dụ), expect sẽ bắt bất kì lỗi nào trong try
try:
    value = 10/0
    num = int(input("Enter a number: "))
    print(num)
except:
    print("Invald input")

try:
    value = 10/0
    num = int(input("Enter a number: "))
    print(num)
except ZeroDivisionError as err:  #bắt lỗi được chỉ định và có thể chỉ định lỗi như 1 giá trị
    print(err)
except ValueError:
    print("Invald Input")