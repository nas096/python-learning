import re


class PhoneNumber:
    def __init__(self, number):
        self.number = number.strip()
        self.number = re.sub("[^0-9]", "", self.number)
        if len(number) == 10:
            if self.number[0] == "0" or self.number[0] == "1":
                raise ValueError("Please enter valid area code")

            pass

        if len(number) == 11:
            pass

        # if len(self.number) <= 9:
        #     raise ValueError("Your phone number must not less than 10 digits")

        # if len(self.number) == 11 and self.number[0] != "1":
        #     raise ValueError("The start of 11 digits phone number must be 1")

        # if len(self.number) > 11:
        #     raise ValueError("Your phone number must not more than 11")

        # if len(self.number) == 10 and (self.number[0] == "1" or self.number[0] == "0"):
        #     raise ValueError(
        #         "Your first digit in your phone number must be from 2 to 9.")

        # if self.number.isnumeric() == False:
        #     raise ValueError("Please enter a valid phone number")

        # if self.number[3] == "0" or self.number[3] == "1":
        #     raise ValueError("Your exchange code must be from 2 to 9")

        # if len(self.number) == 11:
        #     self.number = self.number[1::]

    def pretty(self):
        if self.number[0] == "1":
            self.number = self.number[1::]

        pass

    def area_code(self):
        return self.number[0:2]
