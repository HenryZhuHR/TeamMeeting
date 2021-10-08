import os
import numpy as np
from matplotlib import pyplot as plt

DATA_DIR = '0723/result'
# run-clean-tag-Train_Accuracy.csv
list_attack_method = [
    'clean',
    'fgsm_0_01',
    'fgsm_0_5',
    'fgsm_0_8',
]
list_set_type = ['Train', 'Valid']
list_data_type = ['Loss', 'Accuracy']


def read_csv(csv_file: str):
    with open(csv_file, 'r')as f:
        data_list = []
        for line in f.readlines()[1:]:
            data = line.rstrip().split(',')
            data_list.append([int(data[1]),float(data[2])])
    return data_list

data_dict={}
for data_type in list_data_type:
    for set_type in list_set_type:
        for attack_method in list_attack_method:
            file_name = 'run-%s-tag-%s_%s.csv' % (
                attack_method,  # clean/fgsm
                set_type,  # Train/Valid
                data_type,  # Accuracy/Loss
            )
            print(file_name)
            data=read_csv(os.path.join(DATA_DIR, file_name))

            # print(data)
            x,y=[],[]
            for x_,y_ in data:
                x.append(x_)
                y.append(y_)
            x=np.array(x,dtype=np.int8)
            y=np.array(y,dtype=np.float32)
            plt.plot(x,y)
            plt.xlabel('epoch')
            plt.ylabel(data_type)
            plt.title('%s-%s'%(set_type,data_type))
        plt.legend(list_attack_method)
        # savefig_name=os.path,join(DATA_DIR,'%s-%s-%s.jpg'% (attack_method,set_type,data_type))
        # plt.savefig(savefig_name)
        plt.show()
    