# Write a Python program to concatenate all elements in a list into a string and return it.

lista = [1, 23, 4, 13]

def do_string(x):
    k = ''
    for i in x:
        k += str(i)
    return k

z = do_string(lista)
print(z)