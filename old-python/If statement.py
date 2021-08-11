
is_male = False
is_tall = False
if is_male: # cách dùng if statement :D
    print("You are a male")
else:
    print("You are a female")


if is_male or is_tall: # xét 2 trường hợp nếu cái nào true thì thực hiện, hoặc cả 2 cái true (false hết thì ko print)
    print("You are a male or tall or both")
else:
    print("You neither male nor tall") # bạn ko phải con trai và ko cao :D


if is_male and is_tall: # nếu cả 2 trường hợp đều đúng thì thực hiện còn ko thì ko thực hiện và else (nếu có)
    print("You are a tall male")
elif is_male and not(is_tall): # elif là else if, và từ not() phủ định những j có trong ngoặc (T thành F, F thành T)
    print("You are a short male")
elif is_tall and not(is_male):
    print("You are not a male but are tall")
else:
    print("You are not male and not tall") # bạn ko phải con trai hoặc ko cao hoặc cả hai

