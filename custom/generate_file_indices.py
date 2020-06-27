import random
import os
import subprocess
import sys

def split_data_set(image_dir):

    f_train = open("Images_train.txt", 'w')
    
    for filename in os.listdir(image_dir):
        if(filename.split(".")[1].lower() == "jpg"):                      
            f_train.write(image_dir+'/'+filename+'\n')


split_data_set(sys.argv[1])
