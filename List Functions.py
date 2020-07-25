lucky_numbers = [36 , 4 , 7 , 9 , 10 , 14 , 19]
anime = ["Nisekoi" , "Kaguya-sama" , "Elite classroom" , "Oregairu" , "Tensei Slime" ]
anime.extend(lucky_numbers) # chèn thêm 1 list nữa (mở rộng thêm 1 list nữa)
print(anime)

anime1 = ["Nisekoi" , "Kaguya-sama" , "Elite classroom" , "Oregairu" , "Tensei Slime" ]
anime1.append("Naruto") # chèn thêm 1 giá trị ở cuối cái list
print(anime1)

anime2 = ["Nisekoi" , "Kaguya-sama" , "Elite classroom" , "Oregairu" , "Tensei Slime" ]
anime2.insert(2, "Tenki no Ko") # nêu vị trí cần đặt sau đó đặt thêm 1 giá trị ở vị trí đó (index là vị trí)
print(anime2)

anime2.remove("Tenki no Ko") # loại bỏ 1 giá trị trong list (thêm object)
print(anime2)

print(anime2.index("Nisekoi")) # xác định index

anime2.sort() # sắp xếp theo thứ tự theo bảng chữ cái alphabet
print(anime2)

lucky_numbers.sort() # sắp xếp từ nhỏ đến lớn
print(lucky_numbers)

anime2.pop() # xóa giá trị cuối cùng của list hoặc xóa 1 giá trị trong list(thêm index)
print(anime2)

anime2.clear()# xóa hết toàn bộ giá trị trong list
print(anime2)

anime3 = ["Nisekoi" , "Nisekoi" , "Kaguya-sama" , "Elite classroom" , "Oregairu" , "Tensei Slime" ]
print(anime3.count("Nisekoi")) # đếm số lần giá trị xuất hiện trong list

anime3.reverse() # đảo ngược thứ tự các giá trị của list (tương tự với số, boolean)
print(anime3)

anime4 = anime3.copy() #copy list









