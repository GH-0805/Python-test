languages1 = {"Python", "Java", "C++", "Python", "Java", "JavaScript", "C"}
print("Languages in first set:")
print(languages1)

languages2 = {"Python", "Java", "Ruby"}

print("\nUnion:")
print(languages1.union(languages2))

print("\nIntersection:")
print(languages1.intersection(languages2))

print("\nDifference:")
print(languages1.difference(languages2))

cities = ("Delhi", "Mumbai", "Chennai", "Mumbai", "Kolkata")

print("\nCities:")
print(cities)

print("\nMumbai appears", cities.count("Mumbai"), "times")

print("Index of Chennai:", cities.index("Chennai"))

if "Delhi" in cities:
    print("Delhi is present in the tuple")
else:
    print("Delhi is not present in the tuple")

try:
    cities[0] = "Bangalore"
except TypeError:
    print("Tuples cannot be modified.")