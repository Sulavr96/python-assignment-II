full_file_name = input("Enter a full filename with extension: ")
reference_index = full_file_name.find('.')

file_name = full_file_name[:reference_index]
extension = full_file_name[reference_index:]

print("File name is: ", file_name)
print("Extension is: ", extension)
