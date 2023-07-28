filenames = ["1.Raw data.txt", "2.Reports.txt", "3.Presentation.txt"]

for filename in filenames:
    filename_new = filename.replace('.', '-', 1)
    filenames[filenames.index(filename)] = filename_new


print(filenames)
