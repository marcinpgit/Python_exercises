# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#
# Sample value of n is 5

a = int(input("Podaj liczbę całkowitą: "))

z1 = int('%s'%a)
z2 = int('%s%s'%(a, a))
z3 = int('%s%s%s'%(a, a, a))

int = z1 + z2 + z3
print(int)