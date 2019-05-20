from saber.saber import Saber
from saber.config import Config


CONFIG = Config(filepath = "configs/myconf.ini")


saber = Saber(config = CONFIG)
saber.load_dataset('datasets/NCBI-disease-IOB')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/exp3')

del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/exp3')
saber.load_dataset('datasets/CADEC')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/exp3/final')

### second fold exp2 variation
del saber

saber = Saber(config = CONFIG)
saber.load_dataset('datasets/NCBI-disease-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/exp4')

del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/exp4')
saber.load_dataset('datasets/CADEC/1')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/exp4/final')