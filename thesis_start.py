from saber.saber import Saber
from saber.config import Config


CONFIG50 = Config(filepath = "configs/50.ini")

# ### CADEC + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load_dataset('datasets/thesis/CADEC')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/thesis/cadec')
del saber

# ### BC5CDR-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load_dataset('datasets/thesis/BC5CDR-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
del saber

# ### BC5CDR-DIS-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load_dataset('datasets/thesis/BC5CDR-DIS-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
del saber

# ### BC5CDR-MED-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load_dataset('datasets/thesis/BC5CDR-MED-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
del saber

# ### CADEC => BC5CDR-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load('pretrained_models/thesis/cadec')
saber.load_dataset('datasets/thesis/BC5CDR-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.train()
del saber

# ### CADEC => BC5CDR-DIS-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load('pretrained_models/thesis/cadec')
saber.load_dataset('datasets/thesis/BC5CDR-DIS-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.train()
del saber

# ### CADEC => BC5CDR-MED-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load('pretrained_models/thesis/cadec')
saber.load_dataset('datasets/thesis/BC5CDR-MED-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.train()
del saber
# ### PSYTAR + Health (10) => CADEC (50) => test on CADEC & PSYTAR

# saber = Saber(config = CONFIG_PSY10)
# saber.load_dataset('datasets/PSYTAR')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.build(model_name='MT-LSTM-CRF')
# saber.train()
# saber.save('pretrained_models/psytar10')
# del saber
# saber = Saber(config = CONFIG_CADEC50)
# saber.load('pretrained_models/psytar10')
# saber.load_dataset('datasets/CADEC/2')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.train()
# saber.save('pretrained_models/psytar10_cadec50')

# annotated_psytar = open('oj/PSYTAR/annotated_psytar_exp1.txt', 'w')
# annotated_cadec = open('oj/PSYTAR/annotated_cadec_exp1.txt', 'w')
# plain_text_psytar = open('datasets/PSYTAR/plain_text.txt').readlines()
# plain_text_cadec = open('datasets/CADEC/2/plain_text.txt').readlines()

# annotated_psytar.write(saber.annotate(plain_text_psytar))
# annotated_cadec.write(saber.annotate(plain_text_cadec))
# del saber
# del annotated_psytar
# del annotated_cadec


### CADEC + Health (10) => PSYTAR (50) => test on CADEC & PSYTAR

# saber = Saber(config = CONFIG_CADEC10)
# saber.load_dataset('datasets/CADEC/2')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.build(model_name='MT-LSTM-CRF')
# saber.train()
# saber.save('pretrained_models/cadec10')
# del saber
# saber = Saber(config = CONFIG_PSY50)
# saber.load('pretrained_models/cadec10')
# saber.load_dataset('datasets/PSYTAR')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.train()
# saber.save('pretrained_models/cadec10_psytar50')

# # annotated_psytar = open('oj/PSYTAR/annotated_psytar_exp2.txt', 'w')
# # annotated_cadec = open('oj/PSYTAR/annotated_cadec_exp2.txt', 'w')

# # annotated_psytar.write(saber.annotate(plain_text_psytar))
# # annotated_cadec.write(saber.annotate(plain_text_cadec))
# del saber

