
for letter in "NatGeo Channel": # cho mỗi kí tự trong NatGeo Channel, muốn in ra kí tự đó(ví dụ)
    print(letter)

friends = ["Jim", "Jenny", "Ben"]
for friend in friends: # từ friend có thể thay bằng bất kì từ nào, letter cũng vậy
    print(friend)

for index in range(3, 10): # range là 1 dãy số tăng dần lên từ 0 và ko bao gồm số trong ngoặc (nếu có nhiều số thì ko phải số đằng sau)
    print(index)

for index1 in range(len(friends)):
    print(friends[index1])

for index2 in range(5):
    if index2 == 0:
        print("First Iteration")
    else:
        print("Not first")