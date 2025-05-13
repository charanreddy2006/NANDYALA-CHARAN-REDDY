#task 1:

marks={'Alice':85,'raju':67,'Mike':98,'Charan':99}
name=input("Enter the student's name: ")
if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("Student not found.")


#task 2:

List=[1,2,3,4,5,6,7,8,9,10]
first_five=List[:5]
reversed_five = first_five[::-1]
print("original list: ",List)
print("Extracted first five elementsList: ",List[:5])
print("Reversed extracted elements: ",reversed_five)



