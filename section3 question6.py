# Create and write data to report.txt
with open("report.txt", "w") as file:
    file.write("Rahul-85\n")
    file.write("Priya-90\n")
    file.write("Rohan-78\n")
    file.write("Sneha-92\n")
    file.write("Amit-65\n")

try:
    file = open("report.txt", "r")

    print("Students with marks greater than 80:")
    for line in file:
        name, marks = line.strip().split("-")
        if int(marks) > 80:
            print(name, "-", marks)

except FileNotFoundError:
    print("File not found!")

finally:
    try:
        file.close()
    except NameError:
        pass
    print("File operation completed.")