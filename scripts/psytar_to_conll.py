import re

text = open('../datasets/PSYTAR/text.txt').readlines()
labels = open('../datasets/PSYTAR/labels.txt').readlines()
output = open('../datasets/PSYTAR/text_conll.txt', 'w')

for line_no, line in enumerate(text):
	words = re.sub("[^\S]", " ", line).split()
	tags = re.sub("[^\S]", " ", labels[line_no]).split()
	for word_no, word in enumerate(words):
		output.write(word + "\t" + tags[word_no] + "\n")
	output.write("\n")

print('DONE with conll')

text_conll = open('../datasets/PSYTAR/text_conll.txt', 'r').readlines()
train_size = len(text_conll)*0.8

train = open('../datasets/PSYTAR/train.txt', 'w')
test = open('../datasets/PSYTAR/test.txt', 'w')

for line_no, line in enumerate(text_conll):
	if line_no < train_size:
		train.write(line)
	else:
		test.write(line)

print('DONE with splitting')
