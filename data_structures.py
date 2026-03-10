# Python program to display dictionaries, tuples, and sets

# --- DICTIONARY ---
print("=" * 40)
print("DICTIONARY")
print("=" * 40)

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "languages": ["Python", "JavaScript"]
}

print("Dictionary:", person)
print("\nAccessing values:")
print("  name  :", person["name"])
print("  age   :", person["age"])
print("  city  :", person["city"])

print("\nKeys  :", list(person.keys()))
print("Values:", list(person.values()))
print("Items :", list(person.items()))

print("\nIterating over dictionary:")
for key, value in person.items():
    print(f"  {key} -> {value}")


# --- TUPLE ---
print("\n" + "=" * 40)
print("TUPLE")
print("=" * 40)

coordinates = (10.5, 20.3, 30.7)
fruits = ("apple", "banana", "cherry", "apple", "mango")

print("Coordinates tuple :", coordinates)
print("Fruits tuple      :", fruits)

print("\nAccessing elements:")
print("  coordinates[0] :", coordinates[0])
print("  fruits[-1]     :", fruits[-1])

print("\nSlicing:")
print("  fruits[1:3]    :", fruits[1:3])

print("\nTuple methods:")
print("  fruits.count('apple') :", fruits.count("apple"))
print("  fruits.index('cherry'):", fruits.index("cherry"))

print("\nTuple unpacking:")
x, y, z = coordinates
print(f"  x={x}, y={y}, z={z}")

print("\nIterating over tuple:")
for i, fruit in enumerate(fruits):
    print(f"  [{i}] {fruit}")


# --- SET ---
print("\n" + "=" * 40)
print("SET")
print("=" * 40)

colors = {"red", "green", "blue", "yellow"}
warm_colors = {"red", "orange", "yellow"}

print("Colors set     :", colors)
print("Warm colors set:", warm_colors)

print("\nSet operations:")
print("  Union            :", colors | warm_colors)
print("  Intersection     :", colors & warm_colors)
print("  Difference       :", colors - warm_colors)
print("  Symmetric diff   :", colors ^ warm_colors)

print("\nMembership test:")
print("  'red' in colors  :", "red" in colors)
print("  'pink' in colors :", "pink" in colors)

colors.add("purple")
print("\nAfter add('purple')   :", colors)

colors.discard("green")
print("After discard('green'):", colors)

# Removing duplicates using a set
numbers_with_dupes = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers_with_dupes)
print("\nOriginal list  :", numbers_with_dupes)
print("Unique (set)   :", unique_numbers)
