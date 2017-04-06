import random

#opening the file containing the data (roes.csv)
data_file=open("rows.csv","r")

#the size of the new dataset after it is processed
size_=0

#all the data is read from the file and is stored in a list(data[])
data=[]

#to remove the plasec which contain less than 20 cases of the same cause of death
numbers=list(range(0,20))
numbers=map(str,numbers)
for line in data_file:
    split_line=line.split(',')
    area=split_line[1]
    infection=split_line[2]
    score=split_line[3]
    #getting rid of the examples whith count between 0-20
    if score in numbers:
        continue
    else:
        #turning each example into a list
        temp_data = [area,infection,score]
        data.append(temp_data)
        size_=size_+1

#as the data is very large randomly choosing data points
random.shuffle(data)
rand_data=data[0:10000]

#printing each example as a string which can be redirected into a file
for i in rand_data:
     print(" ".join(i))
