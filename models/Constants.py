import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os
import tensorflow as tf

MAX_FEATURES = 5000
SEQUENCE_LENGTH = 1000
BATCH_SIZE = 16
SEED = 1000
AUTOTUNE = tf.data.AUTOTUNE
VOCAB_SIZE = 1500

data = pd.read_csv("../data/archive/training.1600000.processed.noemoticon.csv", encoding = 'latin', names = ['polarity', 'id', 'date', 'query', 'user', 'text'])

data_directory = os.path.join("../data/archive")