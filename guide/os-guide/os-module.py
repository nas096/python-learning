import os
from datetime import datetime

# print out the current directory
print(os.getcwd())

# Change directory
os.chdir('D:/Programming/Python/guide/os-guide')

print(os.getcwd())

# To know all the files and folders in the the cwd
print(os.listdir())

# Make new directory
	# Create only 1 directory
# os.mkdir('OS-Demo-2')
	# Create multiple directories including the sub-directories
	# Recommend this way to create directories.
# os.makedirs('OS-Demo-4/Sub-Dir-2')

# Delete Directories
	# Remove 1 directory
# os.rmdir('OS-Demo-2')
	# Remove all directories in the path including the parents directory
# os.removedirs("OS-Demo-2/Sub-Dir-1")

# Rename file and folders
# os.rename('demo.txt', 'test.txt')

# print out all the information about a selected file
print(os.stat('test.txt'))


# To get a specific attribute in .stat method
print(os.stat('test.txt').st_mtime) 


# print out the last edited time
mod_time = os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# See the directories tree and files as tuples. This for loop still process until it go through the entire tree in the directory.

# for dirpath, dirnames, filesnames in os.walk("D:/Programming/Python/"):
# 	print('Current Path:', dirpath)
# 	print('Directories:', dirnames)
# 	print("Files: ", filesnames)
# 	print()

# Get all or (specified with .get('environ_name')) specified environment varible
print(dict(os.environ))

# Join 2 path together
print(os.path.join(os.environ.get('APPDATA'), 'test.txt'))


# Create the file (do by yourself)

# print out the basename of a path (no matter the path existed or not)
print(os.path.basename('/tmp/test.txt'))

# print the directory name
print(os.path.dirname('/home/test.txt'))

# print both of those in a tuple
print(os.path.split('/tmp/test.txt'))

# Check the existance of a path
print(os.path.exists('/home/nas'))

# Check if it is a file
print(os.path.isfile('/tmp/fdddddfdf'))

# Check if it is a directory
print(os.path.isdir('/tmp/fsdsfdsf'))

# Split the file path root and the extension in a tuple
print(os.path.splitext('tmp/test.txt'))








