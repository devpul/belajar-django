# set
# otomatis urut
thisset = {"a", "b", "c", True, 1, 2, False}
print(thisset)

for x in thisset:
    print(x)
    
# cara cek tipe data
x = type(thisset)
print(x)

# cara nambah item
# add
# update
# remove
# discard
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
# thisset.discard('orange')
print(thisset)