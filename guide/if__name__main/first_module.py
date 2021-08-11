# print(__name__) # Output: __main__. This print out the file name.
# print(f"First Module's Name: {__name__}")
# Explain: before Python run the file, it will go through the script 
# and set a few specific variables. One of these is __name__. When we
# import a module, it will set the __name__ variable to the name of
# file. So when you run the module-imported file,
# it will print out the "First Module Name..."
# line
# The reason to doing that because the file not
# ran directly, it is being imported.


# def main():
# 	print(f"First Module's Name {__name__}")
# 	pass

# if __name__ == '__main__': # Is this file run directly in Python or it is being imported.
# 	main()

print("This will always be run")

def main():
	print("First Module Main Method")
if __name__ == '__main__':
	print("Run Directly")
else:
	print("Run from Import")