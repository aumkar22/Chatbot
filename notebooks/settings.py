
# coding: utf-8

# In[1]:

import os
import sys
import time
import glob
import numpy as np


# In[ ]:

ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ADD_DATA_DIR = os.path.join(ROOT_DIR, 'AdditionalFiles')
SUBSET_FILE = os.path.join(ADD_DATA_DIR, 'subset_msd_summary_file.h5')
MSD_CODE_PATH = os.path.join(ROOT_DIR, 'MSongsDB')
sys.path.append(os.path.join(MSD_CODE_PATH, 'PythonSrc'))


# In[ ]:

import hdf5_getters as GETTERS


# In[5]:

def apply_to_all_files(ext='.h5'):
    cnt = 0
    # iterate over all files in all subdirectories
    for root, dirs, files in os.walk(DATA_DIR):
        files = glob.glob(os.path.join(root,'*'+ext))
        # count files
        cnt += len(files)
        # apply function to all files
        h5 = []
        for f in files :
            h5.append(GETTERS.open_h5_file_read(f))
        
    return h5

