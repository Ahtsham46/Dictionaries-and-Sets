dictonary = {}
x = int(input("Enter marks of physics: "))
dictonary.update({"phy": x})
x = int(input("Enter marks of math: "))
dictonary.update({"math": x})
x = int(input("Enter marks of Chemistry: "))
dictonary.update({"chem": x})

print(dictonary)


sett = {("float", 9.0, "int", 9)}
print(sett)