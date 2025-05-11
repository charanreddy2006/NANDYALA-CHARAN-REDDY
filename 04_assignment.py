#task 1:
try:
    file = open("sample.txt", "r")
    reading_file = file.read()
    print(reading_file)
    file.close()

except FileNotFoundError:
    print("Error: The File 'sample.txt' was not found")



#task 2:
file = open("sample.txt", "w")
n=str(input("Enter text to write to the file: "))
writing_file = file.write(n)
print(writing_file)
print("Data Successfully written to output.txt")
file.close()


file = open("sample.txt", "a")
n=str(input("Enter additional text to append: "))
appending_file = file.write(n)
print(appending_file)
print("Data Successfully appened ")
file.close()


file = open("sample.txt", "r")
reading_file = file.read()
print(reading_file)
file.close()



