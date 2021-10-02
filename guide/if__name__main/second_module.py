import first_module

first_module.main()
print(f"Second Module's Name: {__name__}")
# Output: __main__ because Python is running this file directly
# Also, if we change the code in the first_module.py file and run this
# file, it won't print out the First Module's Name ... because it is
# being imported to this file. 