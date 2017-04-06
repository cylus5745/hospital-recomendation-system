#import numpy as np
import random

data_file=open("rows.csv","r")
number=0
data=[]
for line in data_file:
    #print(line)
    split_line=line.split(',')
    """if '"Not Available"' in split_line:
        continue
    else:"""
    area=split_line[1]
    #area=area[1:-1]
    infection=split_line[2]
    #infection=infection[1:-1]
    score=split_line[3]
    #score=score[1:-1]
    temp_data = [area,infection,score]
    data.append(temp_data)
    number=number+1
    #print(line)
random.shuffle(data)
rand_data=data[0:10000]
# while(len(rand_data)<10000):
#     temp=random.choice(data)
#     if temp in rand_data:
#         pass
#     else:
#         rand_data.append(temp)
#
# for i in rand_data:
#     print(i)
"""examples=0
key=[0,1]
for line in data:
    if random.choice(key) == 1 and examples<10000:
        examples=examples+1
        print(line)
        rand_data.append(line)
print(len(rand_data))
"""
for i in rand_data:
    print(i)
