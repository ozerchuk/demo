#Task 1


name = input('Enter your name:')
string = len(name)
print('Word \'', name,'\' consists of', string, 'letters')

#Task 2

age = input('Enter you age! it should be a number:')

if age.isdigit():
    age_numeric = int(age)
    if  age_numeric < 1:
        print('Less than 1')
    elif age_numeric > 100:
        print ('More than 100')
    elif '7' in age:
        print('You are lucky')
    elif age_numeric < 7:
        print('Where is your parents?')
    elif age_numeric < 16:
        print('It is film for adult')
    elif age_numeric > 65:
        print('Show your pension certificate')
    else:
        print('There are no tickets')
else:
    print('You input is not a number')