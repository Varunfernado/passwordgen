import random
print('welcome to your password  Generator')

chars = 'abauhfoauebfewafabfagvnaljefnoazifa'

number =input('amount of password to generate:')
number =int(number)

length = input('Indoor password length: ')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
    passwords =''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)





