from Chef import Chef
# inside ChineseChef class, be able to use Chef class
class ChineseChef(Chef): # phải thêm cái Chef nha
    def make_dish(self): # có thể overwrite những gì trong class Chef
        print("The chef makes bbq")
    def make_fried_rice(self):
        print("The chef makes fried rice")