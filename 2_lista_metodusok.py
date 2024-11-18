
nyelvek = ['Python', 'C', 'C++', 'Java', 'Python']
# változóhoz mentve megtartja az eredeti listát is
nyelvek2 = sorted(nyelvek)
print(nyelvek2)
print(nyelvek)

# sorbarendezi a listát - helyben rendez!!!
nyelvek.sort()
print(nyelvek)

# fordított sorrendbe rendezi a listát
nyelvek.reverse()  
print(nyelvek)


# az adott elem első előfordulásának indexe
print(nyelvek.index('C'))
print(nyelvek.index('C++'))

# az adott elem hányszor fordul elő
print(nyelvek.count('Python'))
print(nyelvek.count('Py'))

# NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)
print('C+++' in nyelvek)

nev = "Hello"
print(nev.index("l"))

print(type(nyelvek))
print(type(nev))