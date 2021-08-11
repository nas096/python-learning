# Use this to handle errors:
try:
	f = open("text_file.txt")
	var = bad_var
except FileNotFoundError: # We should at specific at possible so we need to use different messages for different errors.
	# Write a meaningful message to indicate the error
	print("Sorry. This file doesn't exist")

except Exception:
	print("Sorry, something went wrong.")


# To print out the error's message that we hit
try:
	f = open("textfile.txt")
except FileNotFoundError as e:
	print(e)

except Exception as e:
	print(e)

else: # This key word works when the try clause went well and didn't have any errors
	print(f.read())
	f.close()

finally: # This keyword clause runs on matter the code is successful or raise an exception.
	print("Executing Finally...")


# If you want to more interact with the try clause, you can even raise the exception in custom conditions or manually raise exception. For example if the filename is not what you want.
try:
	f = open("nani.txt")
	if f.name == "nani.txt":
		raise Exception

except Exception as e:
	print("Error!")