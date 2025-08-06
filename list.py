

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



