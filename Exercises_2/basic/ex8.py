# Write a program (function!) that takes a list and returns a new list that contains all
# the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list,
# and another using sets.

a = [1, 2, 3, 3, 1, 4, 5, 6, 2, 7, 8, 9, 8, 9]

def duplikaty(x):
    b = []
    for i in x:
        if i not in b:
            b.append(i)
    return b

z = duplikaty(a)
print(z)


