import csv
import pandas as pd
import numpy as np
from random import randrange
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split

test=[]
test2=[]
test_index=[]
zero_class=[]
one_class=[]
final_test=[]
final_test2=[]
final_train=[]


exclude=['065', '120', '127', '134', '232', '279', '465', '514', '574', '596', '700', '767', '373', '325']

with open("Clinical_and_Other_Features_new2.csv", 'r') as f:
    lines=f.readlines()
print(len(lines[0].split(',')))
print(len(lines[1].split(',')))
print(len(lines[2].split(',')))
print(len(lines[3].split(',')))

print("length of lines "+str(len(lines)))

patient_id=[]
not_include_list=[]

for index in range(0, len(lines)):
    patient_id.append(lines[index][0])
    line=lines[index].split(',')
    if '0' in line[42]:
        zero_class.append(index)
    else:
        one_class.append(index)

print("length of zero class "+str(len(zero_class)))
print("length of one class "+str(len(one_class)))

print(len(lines))
rand_index=randrange(len(lines))
print(rand_index)

while len(test)<165:
    rand_index=randrange(len(zero_class))
    if rand_index not in test:
        test.append(rand_index)
        final_test.append(lines[zero_class[rand_index]].split(','))
        test_index.append(zero_class[rand_index])

print("length of final _test "+str(len(final_test)))

while len(test2)<17:
    rand_index2=randrange(len(one_class))
    if rand_index2 not in test2:
        test2.append(rand_index2)
        final_test2.append(lines[one_class[rand_index2]].split(','))
        test_index.append(one_class[rand_index2])

print("length of final _test2 "+str(len(final_test2)))

print(len(test))

for index2 in range(0, len(lines)):
    #print("index "+str(index))
    if index2 not in  test_index:
        #print("come here")
        final_train.append(lines[index2].split(','))

print(len(final_train))

with open('test.csv', 'w', newline='') as f2:
    write = csv.writer(f2)
    for row in final_test+final_test2:
        write.writerow(row)

with open('train.csv', 'w', newline='') as f3:
    write2 = csv.writer(f3)
    for row2 in final_train:
        write2.writerow(row2)
   
print("done")




