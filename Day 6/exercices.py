tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
#--> t1 = (4, 2, 6)
#--> t2 = (1, 5, 3)
def swap_tuples(tuple1, tuple2):
    print("before swap: \n")
    print("tuple1", tuple1)
    print("tuple2", tuple2)
    print("after swap: \n")
    new_tuple1 = (tuple2[0], tuple1[1], tuple2[2])
    new_tuple2 = (tuple1[0], tuple2[1], tuple1[2])

    print("tuple1", new_tuple1)
    print("tuple2", new_tuple2)



swap_tuples(tuple1, tuple2)


#swap lists:
def swap_lists(list1, list2):
    print("before swap: \n")
    print("list1", list1)
    print("list2", list2)

    print("\nafter swap: \n")
    temp = list1[0]
    list1[0] = list2[0]
    list2[0] = temp
    temp = list1[0]
    list1[0] = list2[0]
    