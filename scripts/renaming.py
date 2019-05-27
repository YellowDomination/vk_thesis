import re

# in_main_train = open('../datasets/thesis/BC5CDR-IOB/train.tsv', 'r').readlines()
# in_main_test = open('../datasets/thesis/BC5CDR-IOB/test.tsv', 'r').readlines()
# in_main_devel = open('../datasets/thesis/BC5CDR-IOB/devel.tsv', 'r').readlines()

# in_dis_train = open('../datasets/thesis/BC5CDR-DIS-IOB/train.tsv', 'r').readlines()
# in_dis_test = open('../datasets/thesis/BC5CDR-DIS-IOB/test.tsv', 'r').readlines()
# in_dis_devel = open('../datasets/thesis/BC5CDR-DIS-IOB/devel.tsv', 'r').readlines()

# in_med_train = open('../datasets/thesis/BC5CDR-MED-IOB/train.tsv', 'r').readlines()
# in_med_test = open('../datasets/thesis/BC5CDR-MED-IOB/test.tsv', 'r').readlines()
# in_med_devel = open('../datasets/thesis/BC5CDR-MED-IOB/devel.tsv', 'r').readlines()

in_main_train = open('../datasets/thesis/BioNLP13PC-IOB/train.tsv', 'r').readlines()
in_main_test = open('../datasets/thesis/BioNLP13PC-IOB/test.tsv', 'r').readlines()
in_main_devel = open('../datasets/thesis/BioNLP13PC-IOB/devel.tsv', 'r').readlines()

inputs = [
	in_main_train, 
	in_main_test,
	in_main_devel#,
	# in_dis_train,
	# in_dis_test,
	# in_dis_devel,
	# in_med_train,
	# in_med_test,
	# in_med_devel
]

# out_main_train = open('../datasets/thesis/BC5CDR-IOB/train.txt', 'w')
# out_main_test = open('../datasets/thesis/BC5CDR-IOB/test.txt', 'w')
# out_main_devel = open('../datasets/thesis/BC5CDR-IOB/devel.txt', 'w')

# out_dis_train = open('../datasets/thesis/BC5CDR-DIS-IOB/train.txt', 'w')
# out_dis_test = open('../datasets/thesis/BC5CDR-DIS-IOB/test.txt', 'w')
# out_dis_devel = open('../datasets/thesis/BC5CDR-DIS-IOB/devel.txt', 'w')

# out_med_train = open('../datasets/thesis/BC5CDR-MED-IOB/train.txt', 'w')
# out_med_test = open('../datasets/thesis/BC5CDR-MED-IOB/test.txt', 'w')
# out_med_devel = open('../datasets/thesis/BC5CDR-MED-IOB/devel.txt', 'w')

out_main_train = open('../datasets/thesis/BioNLP13PC-IOB/train.txt', 'w')
out_main_test = open('../datasets/thesis/BioNLP13PC-IOB/test.txt', 'w')
out_main_devel = open('../datasets/thesis/BioNLP13PC-IOB/devel.txt', 'w')

outputs = [
	out_main_train,
	out_main_test,
	out_main_devel#,
	# out_dis_train,
	# out_dis_test,
	# out_dis_devel,
	# out_med_train,
	# out_med_test,
	# out_med_devel
]
for i, fold in enumerate(inputs):
	for line_no, line in enumerate(fold):
		if len(line) > 1:
			words = re.sub("[^\S]", " ", line).split()
			if words[1] == "B-Disease":
				words[1] = "B-DIS"
			if words[1] == "I-Disease":
				words[1] = "I-DIS"
			if words[1] == "B-Chemical":
				words[1] = "B-MED"
			if words[1] == "B-Simple_chemical":
				words[1] = "B-MED"
			if words[1] == "I-Chemical": 
				words[1] = "I-MED"
			if words[1] == "I-Simple_chemical":
				words[1] = "I-MED"
			if words[1] == "B-Gene_or_gene_product":
				words[1] = "B-GGP"
			if words[1] == "I-Gene_or_gene_product":
				words[1] = "I-GGP"
			if words[1] == "B-Complex":
				words[1] = "B-COM"
			if words[1] == "I-Complex":
				words[1] = "I-COM"
			if words[1] == "B-Cellular_component":
				words[1] = "B-CC"
			if words[1] == "I-Cellular_component":
				words[1] = "I-CC"
			outputs[i].write(words[0] + "\t" + words[1] + "\n")
		else:
			outputs[i].write("\n")

print('done')