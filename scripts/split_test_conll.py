import re

test = open('../datasets/PSYTAR/test.txt').readlines()
plain_text = open('../datasets/PSYTAR/plain_text.txt', 'w')
plaint_tags = open('../datasets/PSYTAR/plaint_tags.txt', 'w')

for line_no, line in enumerate(test):
	print(line)
	words = re.sub("[^\S]", " ", line).split()
	if words:
		plain_text.write(words[0] + " ")
		plaint_tags.write(words[1] + " ")

print('DONE with PSYTAR')

test = open('../datasets/CADEC/2/test.txt').readlines()
plain_text = open('../datasets/CADEC/2/plain_text.txt', 'w')
plaint_tags = open('../datasets/CADEC/2/plaint_tags.txt', 'w')

for line_no, line in enumerate(test):
	print(line)
	words = re.sub("[^\S]", " ", line).split()
	if words:
		plain_text.write(words[0] + " ")
		plaint_tags.write(words[1] + " ")

print('DONE with CADEC')