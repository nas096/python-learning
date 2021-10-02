# exercises for python :D, for num in range(int(y/2), 0, -1): # ngoại trừ 0 với -1
# repr: reprint :D
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print(color_list_1.difference(color_list_2)) # in ra sẽ nêu sự khác biệt giữa list1 với list2(in ra sẽ là white và black)

"""
def gcd(x, y):
    if x % y == 0:
        return y
    for num in range(int(y/2), 0, -1): # ngoại trừ 0 với -1
        if x % num == 0 and y % num ==0:
            gcd = num
            break
    return gcd
print("The GCD is " + str(gcd(12, 17)))
# tìm ước chung nhỏ nhất



x = "awesome"

def myfunc():
  global x   # global variables có thể dùng bên trong hoặc ngoài function
  x = "fantastic"
#có thể thay đổi variables bên ngoài ở bên trong functions (dùng global)
myfunc()

print("Python is " + x)



def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break # tạm dừng if statement lại ở đây
       z += 1

   return lcm
print(lcm(4, 6))
print(lcm(15, 17))
# bội số chung nhỏ nhất



def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum
print(sum(5, 12))



x = int(input("Enter x: "))
y = int(input("Enter y: "))
tinh = (x+y)**2
print("({} + {}) ^ 2 = {}".format(x, y, tinh))
# hình như là 1 cách khác của %a :D

"""

import math
x1 = 4
x2 = 0
y1 = 6
y2 = 6
distance = math.sqrt((x1 - y1)**2 + (x2 - y2)**2)
print(distance)
# làm toán trong python
























