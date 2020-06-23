'''
For using this script you need to clone the WordEmbedder.py
!git clone https://github.com/shreyanshchordia/WordEmbedder.git

downloading dependencies
!pip install -r /content/WordEmbedder/requirements.txt
'''

from WordEmbedder.WordEmbedder import Embedder

'''
Substitution Data augmentation
technique 1: Replacing random words from a sentence with <oov> (or <unk>) tag:-(unk_substitutor())
technique 2: Substituting random words with their synonyms:- (word_substitutor())
'''

stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
# thanks to https://gist.github.com/sebleier/554280#gistcomment-2596130

def unk_substitutor(tokenized_sentence, k=1):
    length = len(tokenized_sentence)
    if length <= k:
        return -1
    substitution_list = [random.randint(0,length - 1) for i in range(k)]
    augmented_sentence = [ '<oov>' if i in substitution_list else tokenized_sentence[i] for i in range(len(tokenized_sentence))]
    return augmented_sentence

def word_substitutor(tokenized_sentence, emb, k=2):
    to_be_ignored = stopwords + ['.', '!', ',', '?', ';', ':', '"', "'", '(', ')']
    aug_candidates = [i for i, word in enumerate(tokenized_sentence) if word.lower() not in to_be_ignored]
    augmented_sentence = tokenized_sentence.copy()

    if len(aug_candidates) <= k:
        return -1
    temp = random.choices(aug_candidates, k=k)
    embedding = emb.get_embedder()
    for i in temp:
        word = tokenized_sentence[i].lower()
        check = list(embedding[word].asnumpy())
        if check == [0] * len(check):
            augmented_sentence[i] = '<oov>'
            continue
        else:
            similar_words = emb.most_similar_to(word)
            substitute = random.choice(similar_words)
            augmented_sentence[i] = substitute
            continue
    
    return augmented_sentence


# data augmentation of the tokenized_dataset

# For Q's we use <unk> substitution as well as similar word substitution
# For A's we use similar word substitution only

def data_augmentation(dataset, QuestionAug, AnswerAug, emb, q_k, a_k, min_length):
    '''
    dataset = tokenized list of Q & A

    QuestionAug = 'U' or 'S' that specifies if the augmentation to be performed 
    on Question is <unk> substitution or similar word substitution

    AnswerAug = 'U' or 'S' that specifies if the augmentation to be performed 
    on Answer is <unk> substitution or similar word substitution

    emb = Embedder class object

    q_k = percentage of words to be substituted from the question

    a_k = percentage of words to be substituted from the answer

    min_length = length of the shortest sentence on which augmentation 
    must be performed
    '''
    new_sentences = []
    for pair in dataset:
        
        question, answer = pair[0], pair[1]
        q_output, a_output = None, None

        if len(question) >= min_length:
            
            k = int(len(question) * q_k)

            if QuestionAug == 'U':
                q_output = unk_substitutor(question, k)
                
            elif QuestionAug == 'S': 
                q_output = word_substitutor(question, emb, k)
            
            if q_output == -1:
                q_output = question
        
        else:
            q_output = question


        if len(answer) >= min_length:

            k = int(len(answer) * a_k)

            if AnswerAug == 'U':
                a_output = unk_substitutor(answer, k)

            elif AnswerAug == 'S':    
                a_output = word_substitutor(answer, emb, k)
            
            if a_output == -1:
                a_output = answer
        
        else:
            a_output = answer

        new_sentences.append([q_output, a_output])

    return new_sentences

'''
performing data augmentation on random 300 Q & A's from the dataset
Minimum length for performing data augmentation is set to 4
Percentage of words to be replaced from a sentence is set to 1/3rd
'''

# a very long operation since calculating similar words is costly when it comes to computation
new_sentences = data_augmentation(random.choices(tokenized_dataset, k=300), 'U', 'S', emb, q_k=0.33, a_k=0.33, min_length=4)
