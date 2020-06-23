
# function to normalize string
'''
Involves making tokens more seperable and distinguishable,
for example:
    "What are y'all gonn' do tonight?I hope it's fun or I better leave now!"
        > 'What are y all gonn do tonight ? I hope it s fun or I better leave now !'
'''
import re

def normalize_string(string):
    s = re.sub(r"([.!?])", r" \1 ", string)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    s = re.sub(r"\s+", r" ", s).strip()
    return s


# function to normalize data directory

def normalize_dir(data):
    count = 0
    invalid_count = 0
    dir = dict()

    for __class__ in data.keys():
        for __list__ in data[__class__]:
            temp_list = list()
            for string in __list__:
                count += 1
                try:
                    # here does the normalization occur
                    temp_list.append(normalize_string(string))
                except:
                    invalid_count += 1

            if dir.get(__class__, 0) == 0:
                dir[__class__] = [temp_list]
            
            else:
                dir[__class__].append(temp_list)
    
    print(f'{invalid_count}/{count} were in invalid formats')
    return dir

'''
When the structure of the data directory is somewhat like this:
{
  'POLITICS' :
  [
    [Question, Answer_1, Answer_2, ...],
    ...
    [Question, Answer_1, Answer_2, ...]
  ],
  'GOSSIP' :
  [
    [Question, Answer_1, Answer_2, ...],
    ...
    [Question, Answer_1, Answer_2, ...]
  ],
  ...
  'SCIENCE' :
  [
    [Question, Answer_1, Answer_2, ...],
    ...
    [Question, Answer_1, Answer_2, ...]
  ],
  'LITERATURE' :
  [
    [Question, Answer_1, Answer_2, ...],
    ...
    [Question, Answer_1, Answer_2, ...]
  ],
}
'''
