
monthCoversions = {
    "Jans": "January", # key phải độc nhất, ko đc trùng, có thể là số
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
} # nếu muốn tạo 1 cái dictionary thì phải cho trong ngoặc {}

print(monthCoversions["Nov"])

print(monthCoversions.get("Oct")) # cách khác

print(monthCoversions.get("Luv", "Not a valid Key"))  #có thể dùng not a valid key nếu key ko trùng :D (cũng ko hỉu nữa :)))