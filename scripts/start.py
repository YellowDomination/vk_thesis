from saber.saber import Saber
from saber.config import Config


CONFIG = Config(filepath = "configs/myconf.ini")

##########################################################################################

saber = Saber(config = CONFIG)
saber.load_dataset('datasets/NCBI-disease-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()


del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/NCBI-disease-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/last/first')
del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/last/first')
saber.load_dataset('datasets/CADEC/1')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()


del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/NCBI-disease-IOB')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/last/second')
del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/last/second')
saber.load_dataset('datasets/CADEC/1')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()

##########################################################################################

del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/BC5CDR-chem-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()


del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/BC5CDR-chem-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/last/third')
del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/last/third')
saber.load_dataset('datasets/CADEC/1')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()


del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/BC5CDR-chem-IOB')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/last/fourth')
del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/last/fourth')
saber.load_dataset('datasets/CADEC/1')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()

##########################################################################################

del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/BC5CDR-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()


del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/BC5CDR-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/last/fifth')
del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/last/fifth')
saber.load_dataset('datasets/CADEC/1')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()


del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/BC5CDR-IOB')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/last/sixth')
del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/last/sixth')
saber.load_dataset('datasets/CADEC/1')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()

##########################################################################################

del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/NCBI-disease-IOB')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/last/seventh')
del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/last/seventh')
saber.load_dataset('datasets/CADEC/0', 'datasets/CADEC/1', 'datasets/CADEC/3')
saber.load_embeddings('word_embeddings/Health_2.5mreviews.s200.w10.n5.v15.cbow.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()


del saber
saber = Saber(config = CONFIG)
saber.load_dataset('datasets/NCBI-disease-IOB')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
saber.save('pretrained_models/last/eigth')
del saber
saber = Saber(config = CONFIG)
saber.load('pretrained_models/last/eigth')
saber.load_dataset('datasets/CADEC/0', 'datasets/CADEC/1', 'datasets/CADEC/3')
saber.load_embeddings('word_embeddings/wikipedia-pubmed-and-PMC-w2v.bin')
saber.build(model_name='MT-LSTM-CRF')
saber.train()
