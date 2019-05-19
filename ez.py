from saber.saber import Saber
from saber.config import Config


config = Config(filepath = "configs/myconf.ini")

saber = Saber(config = config)

saber.load_dataset()

saber.load_embeddings()

saber.build() #model_name='MT-LSTM-CRF')

saber.train()

saber.save()