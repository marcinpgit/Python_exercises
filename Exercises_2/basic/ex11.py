# Write a Python program to accept a filename from the user and print the extension of that.

# Sample filename : abc.java
# Output : java

file = input("podaj nazwe pliku do sprawdzenia jego rozszerzenia: ")

file_ext = file.split('.')

print('rozszerzenie pliku to: ', file_ext[-1])
