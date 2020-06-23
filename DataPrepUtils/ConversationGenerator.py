# building the conversation dataset from the directory

# function  to build the Q & A dataset

'''
Takes input of data directory with this structure:
{
  'POLITICS' :
  [
    [Question, Answer_1, Answer_2, ...],
    ...
    [Question, Answer_1, Answer_2, ...]
  ],
  
  ...
  
  'GOSSIP' :
  [
    [Question, Answer_1, Answer_2, ...],
    ...
    [Question, Answer_1, Answer_2, ...]
  ]
}

and returns such a structure:
[
  [Question, Answer_1],
  [Question, Answer_2],
  ...
  [Question, Answer_1],
  [Question, Answer_2],
  ...
]

hence it returns a dataset/ list that has pairs of conversations
'''
def dataset_generator(dir):
    dataset = []
    for __class__ in dir.keys():

        for __list__ in dir[__class__]:

            for i in range(1, len(__list__)):
                # i = 0 has the question

                # __list__[i] can be a list (in case of dir being tokenized)
                # else __list__[i] can be a string (in case of dir being normalized or raw)

                dataset.append([__list__[0], __list__[i]]) # Q & A

    return dataset
