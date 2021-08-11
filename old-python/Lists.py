
friends = ["Bình" , "Huy" , "Quân"] # nếu có [] trong 1 giá trị, python sẽ hiểu là list (array?).

print(friends) #in hết toàn bộ những gì có trong giá trị (valuable)

print(friends[2]) # mỗi giá trị trong list là 1 index (bắt đầu tính từ 0)

print(friends[-2]) # nếu index là số âm thì tính từ dưới lên (bắt đầu từ -1)

friends1 = ["Bình" , "Huy" , "Quân" , "John" , "Peter"] # vẫn là giá trị friends nha :D
print(friends1[1:]) #in từ index 1 trở xuống

print(friends1[1:3]) #in từ index 1 đến 3 (ko bao gồm cả index 3)

friends1[1] = "Ben" # chuyển giá trị trong index thành 1 giá trị khác
print(friends1[1])
