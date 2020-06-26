import re
import pickle
from config import VOCAB_PATH
from Vocab import Vocabulary

def normalize_string(string):
        s = re.sub(r"([.!?])", r" \1 ", string)
        s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
        s = re.sub(r"\s+", r" ", s).strip()
        return s


def tokenize(str):
        return str.split(" ")


def return_vocab_utils(vocab_dict):
    
    vocab = vocab_dict['object']
    word2idx = vocab_dict['word2idx']
    idx2word = vocab_dict['idx2word']

    return vocab, word2idx, idx2word


def return_encoder_decoder(models):

    encoder_model = models['encoder']
    decoder_model = models['decoder']

    return encoder_model, decoder_model

def load_vocabulary():

    file = open(VOCAB_PATH ,'rb')
    vocab_dict = pickle.load(file)
    file.close()

    return vocab_dict