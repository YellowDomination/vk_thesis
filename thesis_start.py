from saber.saber import Saber
from saber.config import Config


CONFIG50 = Config(filepath = "configs/50.ini")

# ### CADEC + Health (50epochs) ###

# saber = Saber(config = CONFIG50)
# saber.load_dataset('datasets/thesis/CADEC')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.build(model_name='MT-LSTM-CRF')
# saber.train()
# saber.save('pretrained_models/thesis/cadec')
# del saber

# ### PSYTAR-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load_dataset('datasets/thesis/PSYTAR-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
del saber

# ### BioNLP13PC-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load_dataset('datasets/thesis/BioNLP13PC-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
del saber

# ### BC5CDR-IOB + Health (50epochs) ###

# saber = Saber(config = CONFIG50)
# saber.load_dataset('datasets/thesis/BC5CDR-IOB')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.build(model_name='MT-LSTM-CRF')
# saber.train()
# del saber

# ### BC5CDR-DIS-IOB + Health (50epochs) ###

# saber = Saber(config = CONFIG50)
# saber.load_dataset('datasets/thesis/BC5CDR-DIS-IOB')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.build(model_name='MT-LSTM-CRF')
# saber.train()
# del saber

# ### BC5CDR-MED-IOB + Health (50epochs) ###

# saber = Saber(config = CONFIG50)
# saber.load_dataset('datasets/thesis/BC5CDR-MED-IOB')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.build(model_name='MT-LSTM-CRF')
# saber.train()
# del saber

# ### CADEC => BC5CDR-IOB + Health (50epochs) ###

# saber = Saber(config = CONFIG50)
# saber.load('pretrained_models/thesis/cadec')
# saber.load_dataset('datasets/thesis/BC5CDR-IOB')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.train()
# del saber

# ### CADEC => BC5CDR-DIS-IOB + Health (50epochs) ###

# saber = Saber(config = CONFIG50)
# saber.load('pretrained_models/thesis/cadec')
# saber.load_dataset('datasets/thesis/BC5CDR-DIS-IOB')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.train()
# del saber

# ### CADEC => BC5CDR-MED-IOB + Health (50epochs) ###

# saber = Saber(config = CONFIG50)
# saber.load('pretrained_models/thesis/cadec')
# saber.load_dataset('datasets/thesis/BC5CDR-MED-IOB')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.train()
# del saber
# ### PSYTAR + Health (10) => CADEC (50) => test on CADEC & PSYTAR

# ### CADEC => BioNLP13PC-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load('pretrained_models/thesis/cadec')
saber.load_dataset('datasets/thesis/BioNLP13PC-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.train()
del saber

# ### CADEC => PSYTAR-IOB + Health (50epochs) ###

saber = Saber(config = CONFIG50)
saber.load('pretrained_models/thesis/cadec')
saber.load_dataset('datasets/thesis/PSYTAR-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.train()
del saber

