import sys, os, random
alph = 'abcdefghijklmnopqrstuvwxyz.-'

try:
    text = str(sys.argv[1])

except:
    print('Usage: ' + sys.argv[0] + ' <input>')
    sys.exit(1)

os.system('clear')


random.seed(text)
text = (random.randint(191115, 919251920))
random.seed(text)
text = (random.randint(1, 10))
random.seed(text)
text = (text / (random.randint(69,420)))
random.seed(text)
text = (text * random.randint(191115, 919251920))
text = round(text)
count = (random.random())


while count > 0:

	text *= text
	count -= 1

text = str(text)
final = ''
for x in text:
	char = (random.randint(0, 9))
	if char == 0:
		char = alph[random.randint(0, 27)]
	if char == 1:
		char = alph[random.randint(0, 27)]
	if char == 2:
		char = alph[random.randint(0, 27)]
	if char == 3:
		char = alph[random.randint(0, 27)]
	if char == 4:
		char = alph[random.randint(0, 27)]
	if char == 5:
		char = alph[random.randint(0, 27)]
	if char == 6:
		char = alph[random.randint(0, 27)] 
	if char == 7:
		char = alph[random.randint(0, 27)] 
	if char == 8:
		char = alph[random.randint(0, 27)] 
	if char == 9:
		char = alph[random.randint(0, 27)]
	char = str(char) 
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))
	if x ==str((random.randint(0, 9))):
		final += char + str((random.randint(0, 9)))



print(final)