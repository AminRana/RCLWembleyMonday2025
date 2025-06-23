# example1/Week 5/ a,b,c,d
#Create a 4D list and print it with tabular form, then add your name,
#age, gender and department as a new staff and print
the list again
print("My List:")
staffmembers = [
    ['John', 40, 'male', 'sales'], ['Smith', 24, 'female', 'marketing'],
    ['Lima', 30, 'female', 'it'], ['Ben', 45, 'male', 'hr'],
    ['Dolly', 55, 'female', 'hr'], ['Jolly', 32, 'female', 'sales'],
    ['Bush', 25, 'male', 'hr'], ['Zen', 20, 'female', 'it'],
    ['Lisa', 60, 'female', 'sales'], ['Chris', 28, 'male', 'marketing']
]

# Display all record from My List
for i, x in enumerate(staffmembers, start=1):
    print(i, x)

# Add name,age,gender,department 
name = input("Type your name to add into list: ").lower()
age = int(input("Type your age: "))
gender = input("Type your gender: ").lower()
dept = input("Type your department: ").lower()
new_record = [name, age, gender, dept]

# Add new member to the end of My List 
staffmembers.append(new_record)  

# Display updated list with the added new member 
for i, x in enumerate(staffmembers, start=1):
    print(i, x)
