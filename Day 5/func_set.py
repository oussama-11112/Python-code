#all ==> check if all items in a set are valid

bool_set = {True, True, False}
print("all items in the set ate true: ", all(bool_set))

#any ==> check if at least one item in a set is valid
bool_set = {True, False, False}
print("if at least one item is valid: ", any(bool_set))