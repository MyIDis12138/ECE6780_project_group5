import csv
import pandas as pd
import numpy as np
from random import randrange
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split

test=[]
test2=[]
test3=[]
test4=[]
test5=[]
test6=[]
test7=[]
test8=[]
zero_class=[]
one_class=[]
fold_1_class_0=[]
fold_1_class_1=[]
fold_2_class_0=[]
fold_2_class_1=[]
fold_3_class_0=[]
fold_3_class_1=[]
fold_4_class_0=[]
fold_4_class_1=[]
final_fold_1_class_1=[]
final_fold_1_class_0=[]
final_fold_2_class_1=[]
final_fold_2_class_0=[]
final_fold_3_class_1=[]
final_fold_3_class_0=[]
final_fold_4_class_1=[]
final_fold_4_class_0=[]
final_fold_5_class_1=[]
final_fold_5_class_0=[]

final_train=[]


exclude=['065', '120', '127', '134', '232', '279', '465', '514', '574', '596', '700', '767', '373', '325']

with open("train.csv", 'r') as f:
    lines=f.readlines()
print(len(lines[0].split(',')))
print(len(lines[1].split(',')))
print(len(lines[2].split(',')))
print(len(lines[3].split(',')))

patient_id=[]
not_include_list=[]

for index in range(0, len(lines)):
    patient_id.append(lines[index][0])
    line=lines[index].split(',')
    if len(line)>1:
        if '0' in line[42]:
            zero_class.append(index)
        else:
            one_class.append(index)

print("length of zero class "+str(len(zero_class)))
print("length of one class "+str(len(one_class)))

print(len(lines))
rand_index=randrange(len(lines))
print(rand_index)

while len(test)<131:
    rand_index=randrange(len(zero_class))
    if rand_index not in test:
        test.append(rand_index)
        final_fold_1_class_0.append(lines[zero_class[rand_index]].split(','))
        fold_1_class_0.append(zero_class[rand_index])

while len(test2)<14:
    rand_index2=randrange(len(one_class))
    if rand_index2 not in test2:
        test2.append(rand_index2)
        final_fold_1_class_1.append(lines[one_class[rand_index2]].split(','))
        fold_1_class_1.append(one_class[rand_index2])

for index2 in range(0, len(fold_1_class_0)):
    zero_class.remove(fold_1_class_0[index2])

for index3 in range(0, len(fold_1_class_1)):
    one_class.remove(fold_1_class_1[index3])


while len(test3)<131:
    rand_index3=randrange(len(zero_class))
    if rand_index3 not in test3:
        test3.append(rand_index3)
        final_fold_2_class_0.append(lines[zero_class[rand_index3]].split(','))
        fold_2_class_0.append(zero_class[rand_index3])

while len(test4)<14:
    rand_index4=randrange(len(one_class))
    if rand_index4 not in test4:
        test4.append(rand_index4)
        final_fold_2_class_1.append(lines[one_class[rand_index4]].split(','))
        fold_2_class_1.append(one_class[rand_index4])

for index4 in range(0, len(fold_2_class_0)):
    zero_class.remove(fold_2_class_0[index4])

for index5 in range(0, len(fold_2_class_1)):
    one_class.remove(fold_2_class_1[index5])

while len(test5)<131:
    rand_index5=randrange(len(zero_class))
    if rand_index5 not in test5:
        test5.append(rand_index5)
        final_fold_3_class_0.append(lines[zero_class[rand_index5]].split(','))
        fold_3_class_0.append(zero_class[rand_index5])

while len(test6)<14:
    rand_index6=randrange(len(one_class))
    if rand_index6 not in test6:
        test6.append(rand_index6)
        final_fold_3_class_1.append(lines[one_class[rand_index6]].split(','))
        fold_3_class_1.append(one_class[rand_index6])

for index6 in range(0, len(fold_3_class_0)):
    zero_class.remove(fold_3_class_0[index6])

for index7 in range(0, len(fold_3_class_1)):
    one_class.remove(fold_3_class_1[index7])

while len(test7)<131:
    rand_index7=randrange(len(zero_class))
    if rand_index7 not in test7:
        test7.append(rand_index7)
        final_fold_4_class_0.append(lines[zero_class[rand_index7]].split(','))
        fold_4_class_0.append(zero_class[rand_index7])

while len(test8)<14:
    rand_index8=randrange(len(one_class))
    if rand_index8 not in test8:
        test8.append(rand_index8)
        final_fold_4_class_1.append(lines[one_class[rand_index8]].split(','))
        fold_4_class_1.append(one_class[rand_index8])

for index8 in range(0, len(fold_4_class_0)):
    zero_class.remove(fold_4_class_0[index8])

for index9 in range(0, len(fold_4_class_1)):
    one_class.remove(fold_4_class_1[index9])


for index10 in range(0, len(zero_class)):
    final_fold_5_class_0.append(lines[zero_class[index10]].split(','))

for index11 in range(0, len(one_class)):
    final_fold_5_class_1.append(lines[one_class[index11]].split(','))


print(len(final_fold_1_class_0))
print(len(final_fold_1_class_1))
print(len(final_fold_2_class_0))
print(len(final_fold_2_class_1))
print(len(final_fold_3_class_0))
print(len(final_fold_3_class_1))
print(len(final_fold_4_class_0))
print(len(final_fold_4_class_1))
print(len(final_fold_5_class_0))
print(len(final_fold_5_class_1))


with open('fold_1_test.csv', 'w', newline='') as f2:
    write = csv.writer(f2)
    for row in final_fold_1_class_1+final_fold_1_class_0:
        write.writerow(row)

with open('fold_1_train.csv', 'w', newline='') as f3:
    write2 = csv.writer(f3)
    for row2 in final_fold_2_class_1+final_fold_2_class_0+final_fold_3_class_1+final_fold_3_class_0+final_fold_4_class_1+final_fold_4_class_0+final_fold_5_class_1+final_fold_5_class_0:
        write2.writerow(row2)

with open('fold_2_test.csv', 'w', newline='') as f4:
    write3 = csv.writer(f4)
    for row3 in final_fold_2_class_1+final_fold_2_class_0:
        write3.writerow(row3)

with open('fold_2_train.csv', 'w', newline='') as f5:
    write4 = csv.writer(f5)
    for row4 in final_fold_1_class_1+final_fold_1_class_0+final_fold_3_class_1+final_fold_3_class_0+final_fold_4_class_1+final_fold_4_class_0+final_fold_5_class_1+final_fold_5_class_0:
        write4.writerow(row4)

with open('fold_3_test.csv', 'w', newline='') as f6:
    write5 = csv.writer(f6)
    for row5 in final_fold_3_class_1+final_fold_3_class_0:
        write5.writerow(row5)

with open('fold_3_train.csv', 'w', newline='') as f7:
    write6 = csv.writer(f7)
    for row6 in final_fold_1_class_1+final_fold_1_class_0+final_fold_2_class_1+final_fold_2_class_0+final_fold_4_class_1+final_fold_4_class_0+final_fold_5_class_1+final_fold_5_class_0:
        write6.writerow(row6)

with open('fold_4_test.csv', 'w', newline='') as f8:
    write7 = csv.writer(f8)
    for row7 in final_fold_4_class_1+final_fold_4_class_0:
        write7.writerow(row7)

with open('fold_4_train.csv', 'w', newline='') as f9:
    write8 = csv.writer(f9)
    for row8 in final_fold_1_class_1+final_fold_1_class_0+final_fold_2_class_1+final_fold_2_class_0+final_fold_3_class_1+final_fold_3_class_0+final_fold_5_class_1+final_fold_5_class_0:
        write8.writerow(row8)

with open('fold_5_test.csv', 'w', newline='') as f10:
    write9 = csv.writer(f10)
    for row9 in final_fold_5_class_1+final_fold_5_class_0:
        write9.writerow(row9)

with open('fold_5_train.csv', 'w', newline='') as f11:
    write10 = csv.writer(f11)
    for row10 in final_fold_1_class_1+final_fold_1_class_0+final_fold_2_class_1+final_fold_2_class_0+final_fold_3_class_1+final_fold_3_class_0+final_fold_4_class_1+final_fold_4_class_0:
        write10.writerow(row10)

print("done")




