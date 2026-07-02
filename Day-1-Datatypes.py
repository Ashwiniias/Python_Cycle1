#Integer
age = 20
marks = 95
print(age,marks)

#float
cgpa = 9.25
price = 499.99
print(cgpa,price)

#string
name = "Ashwini"
branch = "CSE"
college = 'XYZ College'
print(name,branch,college)

#boolean
is_adult=True
is_student=False
print(is_adult,is_student)

#List
marks = [90, 95, 88, 92]
print(marks)

#tuple
colors = ("Red", "Green", "Blue")
print(colors)

#set
numbers = {1, 2, 2, 3, 4}
print(numbers)

#Dict
student = {
    "name": "Ashwini",
    "age": 20,
    "branch": "CSE"
}
print(student["name"])

#Type conversion
a = "10"
b = "20"
print(int(a) + int(b))

#Assigning Multiple variables
a, b, c = map(int, input().split())
print(a + b + c)