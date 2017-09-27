# Write a Python program to get a new string from a given string where "Is" has been
# added to the front. If the given string already begins with "Is" then return the string unchanged.

zdanie = input('Podaj zdanie: ')

if zdanie.startswith('is'):
    print('zdanie zaczyna się na IS')
else:
    print('is ' + zdanie)