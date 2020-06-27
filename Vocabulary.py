# Vocabulary Class
class Vocabulary:
    def __init__(self):
        self.__voc_dict = {
            '<eos>': 0,
            '<oov>': 0,
            '<pad>': 0,
            '<sos>': 0
        }

        self.Vocab = set(['<eos>', '<oov>', '<pad>', '<sos>'])

        self.__trimmed_vocab = None

        self.word2idx = None

        self.idx2word = None
    

    def __addWord(self, word):

        if word in self.Vocab:
            self.__voc_dict[word] += 1
        
        else:
            self.Vocab.add(word)
            self.__voc_dict[word] = 1
        
        return


    def addSentence(self, sentence):

        for word in sentence:
            self.__addWord(word.lower())

        return 


    def minCountTrim(self, min_count):
        
        temp = set(['<eos>', '<oov>', '<pad>', '<sos>'])

        for word in self.__voc_dict.keys():

            if self.__voc_dict[word] >= min_count:
                temp.add(word)
            
            else:
                continue
        
        self.__trimmed_vocab = list(temp)

        return list(temp)


    def wordCountTrim(self, num_words):
        
        temp = set(['<eos>', '<oov>', '<pad>', '<sos>'])

        if num_words <= 4:
            return temp

        sorted_vocab = [k for k,v in sorted(self.__voc_dict.items(),
                                       key=lambda x: x[1],
                                       reverse=True)]
        for word in sorted_vocab:
            if len(temp) == num_words:
                break
            temp.add(word)
        
        self.__trimmed_vocab = list(temp)
        
        return list(temp) 


    def sentence2Sequence(self, sentence):
        
        if self.word2idx is None:
            self.getVocabMapper()
        
        sequence = []
        for word in sentence:
            sequence.append(self.word2idx.get(word.lower(), self.word2idx['<oov>']))
        
        return sequence


    def sequence2Sentence(self, sequence):
        
        if self.idx2word is None:
            self.getVocabMapper()
        
        sentence = []
        for i in sequence:
            sentence.append(self.idx2word[i])
        
        return sentence


    def getTrimmedVocab(self):

        if self.__trimmed_vocab is not None:
            return self.__trimmed_vocab
        else:
            return None


    def getVocabMapper(self):

        vocab = None
        self.word2idx = {
            '<pad>': 0,
            '<oov>': 1,
            '<sos>': 2,
            '<eos>': 3
            }
        self.idx2word = {
            0: '<pad>',
            1: '<oov>',
            2: '<sos>',
            3: '<eos>'
        }
        
        if self.__trimmed_vocab is None:
            vocab = self.Vocab
        
        else:
            vocab = self.__trimmed_vocab
        
        i = 0
        for word in sorted(vocab):
            if word not in ('<pad>', '<oov>', '<eos>', '<sos>'):
                self.word2idx[word] = i + 4
                self.idx2word[i + 4] = word
                i += 1
        
        return self.word2idx, self.idx2word


    def getCountDictionary(self):
        
        return self.__voc_dict
        
        
        
