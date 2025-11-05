##11. Read & Write to a File
####file reading
filepath = "/home/purniema/Documents/python/test.txt"
s_append = "\n Append this to file"
s_write = "New Text"

def file_read(fp):
    f = open(filepath, 'r')
    file_content = f.read()
    print(file_content)
    f.close()

def file_append(fp, s):
    f = open(filepath, 'a')
    f.write(s)

def file_write(fp, s):
    f = open(filepath, 'w')
    f.write(s)

file_read(filepath)
file_append(filepath, s_append)
file_read(filepath)
file_write(filepath, s_write)
file_read(filepath)