file = open('C:\\Users\\mehta\\OneDrive\\Documents\\Python_mega\\members.txt', 'r')
file_data = file.readlines()
user_input = input('enter new member : ') + "\n"
file_data.append(user_input)
file = open('C:\\Users\\mehta\\OneDrive\\Documents\\Python_mega\\members.txt', 'w')
file.writelines(file_data)
file.close()

