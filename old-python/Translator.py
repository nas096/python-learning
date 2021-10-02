
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))

def validate_pin(pin):
    if pin == "1234":
        return True
        print("That's right")
    else:
        return False
        print("Its wrong")
    
    
    #return true or false
    
print(validate_pin(input("Enter your phrase")))

