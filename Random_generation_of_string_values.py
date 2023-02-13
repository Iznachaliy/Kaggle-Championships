import random
import string

# printing 11 lowercase letters
letters = string.ascii_lowercase
print(''.join(random.choice(letters) for i in range(11)))

#printing 12 uppercase letters
letters = string.ascii_uppercase
print(''.join(random.choice(letters) for i in range(12)))

#printing 13 both lowercase and undercase letters
letters = string.ascii_letters
print(''.join(random.choice(letters) for i in range(13)))

#printing 14 digits
letters = string.digits
print(''.join(random.choice(letters) for i in range(14)))

#printing 15 punctuation symbols
letters = string.punctuation
print(''.join(random.choice(letters) for i in range(15)))
