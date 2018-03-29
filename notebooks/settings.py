
# coding: utf-8

# In[1]:

import os
import sys
import glob


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
    h5 = []
    for root, dirs, files in os.walk(DATA_DIR, topdown = True):
        files = glob.glob(os.path.join(root,'*'+ext))
        # count files
        #print(root)
        #print(dirs)
        cnt += len(files)
        # apply function to all files
        #if cnt == 1000:
            #break
        #else:
        
        for f in files:
            #print(f)
            h5.append(f)
        #print(h5)
    return h5

#apply_to_all_files()