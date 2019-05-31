from saber.saber import Saber
from saber.config import Config


CONFIG = Config(filepath = "configs/baseline.ini")


saber = Saber(config = CONFIG)
saber.load_dataset('datasets/NCBI-disease-IOB')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
an = saber.annotate("Privet kak dela sick headacke by MK2 promotes the ubiquitination of p53")
print(an)
