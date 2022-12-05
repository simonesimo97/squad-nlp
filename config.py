import os.path as osp
from pickle import TRUE

# ##########
# FILE PATHS
# ##########
EMBEDDING_PATH = osp.join("data", "embedding_model.pkl")
DATA_PATH = osp.join("data", "training_set.json")
GLOVE_WEIGHTS_PATH = osp.join("data", "glove", "weights")
BERT_WEIGHTS_PATH = osp.join("data", "bert", "weights")
BIDAF_WEIGHTS_PATH = osp.join("data", "bidaf", "weights")

# #########
# CONSTANTS
# #########
ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~–—'
EMPTY_TOKEN = '<EMPTY>'
PAD_TOKEN = '<PAD>'
PAD_POS = 'PAD'
VAL_SPLIT_INDEX = 350

# ###################
# GLOVE CONFIGURATION
# ###################
EMBEDDING_MODEL_TYPE = 'glove'
EMBEDDING_DIMENSION = 300
MAX_CONTEXT_LEN = 400
MAX_QUEST_LEN = 40

# ##################
# BERT CONFIGURATION
# ##################
BERT_SAVE_DIR = 'bert_base_uncased'
BERT_MODEL = 'bert-base-uncased'
BERT_MAX_LEN = 429
TRANSL_DICT = {"'": "''", "-": '--', ':': ':', '(': '(', ')': ')', '.': '.', ',': ',', '`': '``', '$': '$'}

# ###################
# MODEL CONFIGURATION
# ###################
WORKERS = 4
LEARNING_RATE = 5e-5
EPOCHS = 25
BATCH_SIZE = 64
LSTM_UNITS = 250

# ###################
# BIDAF CONFIGURATION
# ###################

CONV_LAYERS = [[150, 10],
               [150, 7],
               [150, 5],
               [150, 3]]
FULLY_CONNECTED_LAYERS = [1024, 1024]
CONCAT_EMBEDDING_DIMENSION = 600
MAX_WORD_LEN = 15
NUM_HIGHWAY = 2
CHAR_WEIGHTS_PATH = osp.join("data", "bidaf", "weights", "CNN_150_FineTunedEmbedding.h5")
LR_REDUCER_RATE = 0.8