
 # mở file ngoài python, mode 1: "r" read (chức năng như cái tên)
 #mode 2:  "w" write, mode 3: "a" apend (thêm vào cuối file chứ ko đc chỉnh sửa, "r+" xem với sửa)

text = open("Text", "r") # có thể chứa trong 1 giá trị

print(text.readable()) # kiểm tra xem file đó có đọc được ko

print(text.readline()) # in ra màn hình những dòng chỉ định

print(text.readlines()[1]) # in file ra màn hình theo dạng list, có thể specify bất kì dòng nào

print(text.read()) # in ra màn hình để cho ta đọc

for lines in text.readlines(): # có thể bỏ vào for loop
    print(lines)

text.close() # đóng file lại



