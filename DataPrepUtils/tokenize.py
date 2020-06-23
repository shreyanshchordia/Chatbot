# function to tokenize a normalized string

def tokenize(str):
    return str.split(" ")

# function to tokenize data directory

'''
Use normalize.py to normalize entire directory before tokenizing
When the structure of the data directory is somewhat like this:
{
  'POLITICS' :
  [
    [Normalized Question, Normalized Answer_1, Normalized Answer_2, ...],
    ...
    [Normalized Question, Normalized Answer_1, Normalized Answer_2, ...]
  ],
  'GOSSIP' :
  [
    [Normalized Question, Normalized Answer_1, Normalized Answer_2, ...],
    ...
    [Normalized Question, Normalized Answer_1, Normalized Answer_2, ...]
  ],
  ...
  'SCIENCE' :
  [
    [Normalized Question, Normalized Answer_1, Normalized Answer_2, ...],
    ...
    [Normalized Question, Normalized Answer_1, Normalized Answer_2, ...]
  ],
  'LITERATURE' :
  [
    [Normalized Question, Normalized Answer_1, Normalized Answer_2, ...],
    ...
    [Normalized Question, Normalized Answer_1, Normalized Answer_2, ...]
  ]
}
'''
def tokenize_dir(data):
    dir = dict()

    for __class__ in data.keys():
        for __list__ in data[__class__]:
            temp_list = list()
            for string in __list__:
                
                # here we tokenize
                temp_list.append(tokenize(string))
                # tokenization and normalization can even be combined
                # I just wanted to keep things more elaborate

            if dir.get(__class__, 0) == 0:
                dir[__class__] = [temp_list]
            
            else:
                dir[__class__].append(temp_list)
    
    return dir
