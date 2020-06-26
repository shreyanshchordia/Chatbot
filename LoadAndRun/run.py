import re
import numpy as np
import random
from config import *
from load_model import load_model
from utils import *
from keras.preprocessing.sequence import pad_sequences

# from keras.models import Model
# from keras.layers import Input, LSTM, Dense, Bidirectional, TimeDistributed, Embedding, Average
# from keras import regularizers, optimizers


def preprocessing(sentence, vocab_object):

    normalized_sentence = normalize_string(sentence)

    tokenized_sentence = tokenize(normalized_sentence)

    if(len(tokenized_sentence)>28):
        # since we can only include 30 words 
        # after including <sos> and <eos>
        tokenized_sentence = tokenized_sentence[:28]
    
    # adding SOS and EOS
    tokenized_sentence.insert(0, SOS)
    tokenized_sentence.append(EOS)

    # padding sentence
    padded_sentence = pad_sequences([tokenized_sentence], maxlen=MAX_LENGTH,
                                    padding='post', dtype=object, value=PAD)[0]

    # converting to sequence
    # It is using the vocab object that has the trimmed vocabulary
    # of 2000 words, for generating the sequence
    sequence = vocab_object.sentence2Sequence(padded_sentence)
    
    # returning numpy array 
    return np.asarray(sequence).reshape(1,-1)



def inference(models, vocab_dict, sentence, random_sample=False):

    encoder_model, decoder_model = return_encoder_decoder(models)

    vocab, word2idx, idx2word = return_vocab_utils(vocab_dict)

    # preprocessing the input to make it feedable to the network
    encoder_input = preprocessing(sentence, vocab)

    # Getting encodings for the input sequences
    h1, c1, h2, c2 = encoder_model.predict(encoder_input)
    states_value = [h1, c1, h2, c2]

    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 1))

    # Populate the first character of target sequence with the start character.
    target_seq[0, 0] = word2idx[SOS]

    # initially decoded sentence is empty
    decoded_sentence = ''

    # to make sure that length of output doesnt extend MAX_LENGTH
    count = 0

    # returns an array of values from 0 to VOCAB_SIZE - 1 (reqd for random sampling)
    vocab_array = np.arange(0, VOCAB_SIZE, 1)

    while True:

        # generating the next prediction for a sequence
        output_tokens, out_h1, out_c1, out_h2, out_c2 = decoder_model.predict([target_seq] + states_value)

        # Sample a token
        # either using 
        # 1. random sampling (helps in generating everytime you run the code)
        # 2. greedy method (you will always get the same output for the same model)
        if random_sample == True:
            sampled_token_index = random.choices(vocab_array,
                                                 weights = list(output_tokens[0, -1, :]))[0]
        else:
            sampled_token_index = np.argmax(output_tokens[0, -1, :])
        
        sampled_char = idx2word[sampled_token_index]
        if(sampled_char == '<eos>'):
            break

        decoded_sentence += sampled_char 
        decoded_sentence += ' '
        count+=1

        # Exit condition: either hit max length
        # or find stop character.
        if (count == MAX_LENGTH):
            break

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index

        # Update states
        states_value = [out_h1, out_c1, out_h2, out_c2]

    return decoded_sentence

def main():

    encoder = load_model('Encoder', ENCODER_MODEL, ENCODER_WEIGHTS)
    decoder = load_model('Decoder', DECODER_MODEL, DECODER_WEIGHTS)

    models = {'encoder': encoder, 'decoder':decoder}

    vocab_dict = load_vocabulary()

    while True:

        question = input()

        answer = inference(models, vocab_dict, question, random_sample=False)

        print(f'\n{answer}\n')
    
    return

if __name__ == "__main__":
    main()

    