temperatures = [10, 12, 14]

temp_str = [str(i) +'\n' for i in temperatures]

file = open("filename1.txt", 'w')

file.writelines(temp_str)