from Set_BSTBased import Set

def show_set(set, set_name):
    print(set_name + ": ", end="")
    for element in set:
        print(element, end=" ")
    print("")

def even_predicate(element):
    return (element % 2) == 0

def over50_predicate(element):
    return element > 50

def map_times_10(element):
    return element * 10

def map_mod_10(element):
    return element % 10

def symetric_difference(setA, setB):
    return setA.difference(setB).union(setB.difference(setA))

def intersect_all(sets):
    if len(sets) == 0:
        return Set()
    result = sets[0]
    for s in sets[1:]:
        result = result.intersection(s)
    return result

setA = Set()
setA.add(95)
setA.add(64)
setA.add(19)
setA.add(67)
setA.add(-24)
setA.add(90)
setB = Set()
setB.add(67)
setB.add(90)
setB.add(67)
setB.add(42)
setB.add(-84)
setC = Set()
setC.add(19)
setC.add(42)
setC.add(67)
sets = [setA, setB, setC]

# Display the 2 sets
show_set(setA, "Set A")
show_set(setB, "Set B")

# Perform union, intersection, and difference of 2 sets
show_set(setA.union(setB), "A union B")
show_set(setA.intersection(setB), "A intersect B")
show_set(setA.difference(setB), "A - B")
show_set(setB.difference(setA), "B - A")

# Perform various filter operations
show_set(setA.filter(even_predicate), "Set A filtered for evens")
show_set(setB.filter(even_predicate), "Set B filtered for evens")
show_set(setA.filter(over50_predicate), "Set A filtered for elements > 50")
show_set(setB.filter(over50_predicate), "Set B filtered for elements > 50")

# Perform various map operations
show_set(setA.map(map_times_10), "Set A mapped * 10")
show_set(setB.map(map_times_10), "Set B mapped * 10")
show_set(setA.map(map_mod_10), "Set A mapped % 10")
show_set(setB.map(map_mod_10), "Set B mapped % 10")

# Perform symetric difference
show_set(symetric_difference(setA, setB), "Symetric Difference A <> B")

# Perform intersection of all sets
show_set(intersect_all(sets), "Intersection of A, B, and C")

test_list = [5, 3, 8, 6, 2, 7, 4, 1, 2, 7, 4, 1]
listSet = Set()
for value in test_list:
    listSet.add(value)
print("Set created from list:", end=" ")
for element in listSet:
    print(element, end=" ")
print()

stringA = "santa"
stringB = "satan"
setStringA = Set()
for char in stringA:
    setStringA.add(char)
setStringB = Set()
for char in stringB:
    setStringB.add(char)
print(setStringA.intersection(setStringB) == setStringB)

setOrdered = set()
for i in range(0, 10):
    setOrdered.add(i)
setMissing = Set()
for i in range(0, 10):
    if i == 5:
        continue
    setMissing.add(i)
print(setOrdered.difference(setMissing))




