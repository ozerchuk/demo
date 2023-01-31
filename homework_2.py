
#Task 1

#first case
country = 'Ukraine'
check_a = country.isalpha()
print('\'Ukraine\' is a word ---->' , check_a)
word = len(country)
print('Length of word \'', country,'\' consists of', word, 'letters')


#second case
name = input()
check_b = name.isalpha()
print('\'',name,'\' is a word ---->',check_b)
string = len(name)
print('Word \'', name,'\' consists of', string, 'letters')

#Task 2

age = int(input('Enter you age:'))

if age < 7:
    print('Where is your parents?')
elif age < 16 and age > 7:
    print('It is film for adult')
elif age > 65 and age < 100:
    print('Show your pension certificate')
elif age == 7:
    print('You are lucky')
else:
    print('There are no tickets')


















