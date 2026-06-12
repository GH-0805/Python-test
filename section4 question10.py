students = {
    "Rahul": {"age": 20, "marks": 85},
    "Priya": {"age": 19, "marks": 90},
    "Rohan": {"age": 21, "marks": 78}
}

students["Sneha"] = {"age": 20, "marks": 92}

students["Rahul"]["marks"] = 88

del students["Rohan"]

if "Priya" in students:
    print("Priya exists in the dictionary")

print("\nKeys:")
for key in students.keys():
    print(key)

print("\nValues:")
for value in students.values():
    print(value)

print("\nItems:")
for item in students.items():
    print(item)

names = list(students.keys())

print("\nList of student names:")
print(names)