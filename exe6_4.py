filenames = ['filename1', 'filename2', 'filename3']

for filename in filenames:
    name = filename + '.txt'
    file = open(name, 'w')
    file.writelines('Hello')
    file.close()
