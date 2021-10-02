"""
text = open("Text", "a") # nếu dùng w như vậy thì nó sẽ xóa hết file và ghi đè :v
text.write("\nhello world")# phải \n nữa ko thì ăn ... :D
text.close() #  dùng phải cẩn thận nữa :D



text1  = open("Text1.py", "w") # nếu dùng tên khác thì nó sẽ tạo ra 1 file mới (dùng w), dùng w cũng có thể tạo ra 1 .abc mới
text1.write("print(hello world)")
text1.close()

"""

