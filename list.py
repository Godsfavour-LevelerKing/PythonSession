# This is a list of 3 names

students = ["Favour", "Temitope", "Fatiha"]

print(students[1]) 


print(students)

 
#
        #ASSIGNMENT
#Create a list of 3 best friends 'name'
#Print the second name
#Print the whole list


#Adding, removing, and Changing Items

students.append("Anab")
print(students)

#Remove

students.append("Table")
students.append("chair")

print(students)

students.remove("Table")

print(students)

students.pop()

print(students)

#change item
students[0] = "Abosede"

print(students)


# Assignment
# Create a foodlist
# add a new food
# change a food
# Print all the food


# Loop with list

for student in students:
    print("Hello", student)

# Assignment
# Create a list of 5 colours. Use a loop to print:
# "I like the colour" for each colour in the list "


students.sort()

print(students)



pupils = []

while True:
    name = input("Enter Student Name (or 'done' to stop): ")
    if name.lower() == "done":
        break
    pupils.append(name)


print("Registered Students:")

for child in pupils:
    print("-", child)


# Assignment
# Add code to remove a student name.
# Make sure students are not reistered twice (if if to check).
# Print the total number of students registered



