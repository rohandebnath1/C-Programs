myfile = open(r"E:\Python Files\File3.txt")
line_count = 0
data = myfile.readlines()
for line in data:
    if line[0] == 'T':
        line_count += 1
print(line_count)
myfile.close()