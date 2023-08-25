names = {'ranim', 'rania', 'rawen'}
names.add('imen') #only adds one item
names.discard('ranim') #delete

other_names = ("anas", "chahd")
print("names before update:\n")
print(names)

names.update(other_names) # add many items/ a list of items at a time.
print("names after update:\n")
print(names)