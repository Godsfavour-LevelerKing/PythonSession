#Normal tuple
colours = ("Red", "Blue", "Green")

# One Itemed Tuple, Add a comma!

solo = ("OnlyOne",)

# Tuple without brackets (optional, but possible)
nums = 1, 2, 3


print(colours[2])


for tpl in colours:
    print(tpl)


# Tuple Challenge - Lock My ID

name = input("Enter Your Name: ")

student_id = input("Enter your ID: ")

identity = (name, student_id)

print("Student Identity Locked:")
print(identity)


print("---------------------Unpacking Tuple-----------------------------")

identify = ("Favour", "STU2031")

names, ID = identify

print("Welcome", names)
print("Your ID is", ID)


# ASSIGNMENT CHALLENGE

# Create a tuple of 3 courses you are taking on PLP
# Try to change one. What error do you get?
# Write code that loops through your tuple and prints:
# "I am currently studying [course]"
# Build a program that accepts 3 quiz scores, stores them in a tuple, and display the average.
