"""
File Handling

var_name = open("file_name","operation")

operation
----------
1) r ---> read
2) a ---> append
3) w ---> write , overwrite
4) x ---> new file creation

var_name.close()
"""

# f = open("demofile.txt","r")

# print(f.read())
# # print(f.read(10))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open("demofile.txt","a")

# f.write("HI! I am additional content")

# f.close()

# f = open("demofile.txt","w")

# f.write("oops! no content is available")

# f.close()

# f = open("file.txt","w")

# f.write("New File Created")

# f.close()

# f = open("file1.txt","x")
# f.write("I am a new file created with 'x'")
# f.close()

# f = open("demofile.txt","x")
# f.write("Hey")
# f.close()

# f = open("myself.txt","w")

# for i in range(10):
#     n = input("Enter Number:")
#     f.write(n)


# f.close()

# f = open("myself.txt","r")
# m = f.read()
# for i in m:
#     j = int(i)
#     if j%2==0:
#         print(j)
# f.close()

import os

os.remove("demofile.txt")

f = open("demofile.txt","r")