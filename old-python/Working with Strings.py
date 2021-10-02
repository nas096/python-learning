# Đọc theo thứ tự nha :D
print("Discovery\nChannel") # xuống hàng

print("Discovery\"Channel") # thêm dấu " trong string (mấy dấu khác làm tương tự, kể cả dấu \)

phrase = "NatGeo Channel"
print(phrase + " is cool.") #nhìn là hiểu r :))

print(phrase.lower()) # chuyển hết thành chữ thường

print(phrase.upper()) # chuyển hết thành chữ in hoa

print(phrase.isupper()) # phrase đó nó có in hoa hết hay ko (True or False), tương tự với lowercase

print(phrase.upper().isupper()) # đổi thành upper rồi kt xem có phải upper hết hay ko (True or False) tương tự với lowercase

print(len(phrase)) # đếm số chữ (characters)

print(phrase[0]) # chuyển số thứ tự của chữ cái thành chữ (bắt đầu từ 0)

print(phrase.index("N")) # chuyển chữ thành số thứ tự của chữ cái (bắt đầu từ 0), nhớ thêm dấu "
# nếu như là 1 dãy kí tự thì sẽ chỉ chuyển chữ đầu tiên

print(phrase.replace("NatGeo", "Discovery")) #thay từ trong ngoặc

# có thể bổ sung thêm
