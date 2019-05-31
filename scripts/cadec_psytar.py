from saber.saber import Saber
from saber.config import Config


CONFIG_PSY 		= Config(filepath = "configs/psytar_cadec_50.ini")
CONFIG_CADEC 	= Config(filepath = "configs/cadec_psytar_50.ini")


### PSYTAR + Health (10) => CADEC (50) + test on PSYTAR

# saber = Saber(config = CONFIG_CADEC)
# saber.load('pretrained_models/psytar10')
# saber.load_dataset('datasets/psytar_cadec')
# saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
# saber.train()
# del saber

### CADEC + Health (10) => PSYTAR (50) + test on CADEC

saber = Saber(config = CONFIG_PSY)
saber.load('pretrained_models/cadec10')
saber.load_dataset('datasets/cadec_psytar')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.train()
del saber