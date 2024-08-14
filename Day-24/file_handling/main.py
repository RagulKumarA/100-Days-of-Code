# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
# with open("my_file.txt", "w") as file:
#     file.write("\n hello boss")

with open(r"C:\Users\Ragul\Desktop\my_file_new.txt","r") as file:
    contents = file.read()
    print(contents)

with open("/Users/Ragul/Desktop/my_file_new.txt","r") as file:
    contents = file.read()
    print(contents)

with open("/../../file_handling/pythonProject/my_file.txt","r") as file:
    contents = file.read()
    print(contents)