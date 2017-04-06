import numpy as np

data_file=open("hospital_data.csv","r")
number=0
data=[]
for line in data_file:
    #print(line)
    split_line=line.split(',')
    if '"Not Available"' in split_line:
        continue
    else:
        area=split_line[0]
        area=area[1:-1]
        infection=split_line[2]
        infection=infection[1:-1]
        score=split_line[3]
        score=score[1:-1]
        temp_data = [area,infection,score]
        data.append(temp_data)
        number=number+1
"""print("number of lines: ",number)
for i in range(0,len(data)):
    print(data[i])
for i in data:
    print i"""
s=" "
for i in data:
    print(s.join(i))
