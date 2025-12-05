# dictionary
thisdict = {
    "name"  : "ibnu",
    "age"   : 21,
}

print(thisdict['name'])
print(thisdict.get('age'))

# loop dict
for x,y in thisdict.items():
    print(x, y)