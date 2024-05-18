# file=open('fileName.txt')

# reads the file
# file.read()

# sets the cursor to the beginning of the file
# file.seek(0) #cursor is set to the beginning of the file

# close the file
# file.close()

# check if file is closed
# file.closed


# with statement
# *acts as a interface to the file
# with open('fileName.txt') as file:
#     file.read()

# write to file
with open('fileName.txt', 'w') as file:
    file.write('Hello World')

# flags
# 'r' - read
# 'r+' - read and write
# 'w' - write
# 'w+' - write and read
# 'a' - append
# 'a+' - append and read
# 'b' - binary
# 'x' - create
# 'rb' - read binary
# 'wb' - write binary
# 'rb+' - read and write binary

# to learn more about files run following command in terminal
# *help(file)
