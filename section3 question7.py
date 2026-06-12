import os
file=open("employees.txt","w")
file.write("john\n")
file.write("jane\n")
file.write("bob\n")
file.close()

file=open("employees.txt","r")
print(file.read())
file.close()

file=open("employees.txt","a")
file.write("alice\n")
file.close()

del file
os.remove("employees.txt")

print(os.path.exists("employees.txt"))