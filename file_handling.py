# to open a file
file = open('demo.txt','r')
data = file.read()
# to close the file to avoid buffer
file.close()
print(data)
# to print all lines as list
# 
#  
# lines_=file.readlines()
# print(lines_)

# write a file
file = open('demo.txt','w')
file.write('this is demo file')
file.writelines([
    'this is file1'
    'this is file2'
])
file.close()

# append a file
file = open('demo.txt','a')
file.write('this is a demo file2')
file.close()