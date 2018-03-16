
# coding: utf-8

# In[10]:

import os
import sys
import time
import glob
import datetime
import sqlite3
import numpy as np
import hdf5_getters as GETTERS


# In[7]:

msd_subset_path='C:/Aumkar/Data Science Masters/Sem 4/Cognitive Computational Modeling of Language and Web Interaction/Assignment 3/wg4-chatbot/MillionSongSubset'
msd_subset_data_path=os.path.join(msd_subset_path,'data')
msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
assert os.path.isdir(msd_subset_path),'wrong path'


# In[8]:

msd_code_path='C:/Users/HP/Documents/GitHub/MSongsDB'
assert os.path.isdir(msd_code_path),'wrong path'


# In[9]:

sys.path.append(os.path.join(msd_code_path,'PythonSrc'))


# In[11]:

def strtimedelta(starttime,stoptime):
    return str(datetime.timedelta(seconds=stoptime-starttime))


# In[12]:

def apply_to_all_files(basedir,func=lambda x: x,ext='.h5'):
    cnt = 0
    # iterate over all files in all subdirectories
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        # count files
        cnt += len(files)
        # apply function to all files
        for f in files :
            func(f)       
    return cnt


# In[13]:

print('number of song files:', apply_to_all_files(msd_subset_data_path))


# In[14]:

all_artist_names = set()


# In[15]:

def func_to_get_artist_name(filename):
    h5 = GETTERS.open_h5_file_read(filename)
    artist_name = GETTERS.get_artist_name(h5)
    all_artist_names.add( artist_name )
    h5.close()


# In[18]:

t1 = time.time()
apply_to_all_files(msd_subset_data_path, func=func_to_get_artist_name)


# In[19]:

t2 = time.time()
print('all artist names extracted in:', strtimedelta(t1,t2))


# In[21]:

print('found',len(all_artist_names),'unique artist names')

for k in range(5):
    print(list(all_artist_names)[k])


# In[22]:

conn = sqlite3.connect(os.path.join(msd_subset_addf_path, 'subset_track_metadata.db'))


# In[23]:

q = "SELECT DISTINCT artist_name FROM songs"


# In[24]:

t1 = time.time()
res = conn.execute(q)


# In[25]:

all_artist_names_sqlite = res.fetchall()
t2 = time.time()


# In[26]:

print('all artist names extracted (SQLite) in:',strtimedelta(t1,t2))


# In[27]:

conn.close()


# In[29]:

for k in range(5):
    print(all_artist_names_sqlite[k][0])


# In[34]:

conn = sqlite3.connect(os.path.join(msd_subset_addf_path, 'subset_track_metadata.db'))


# In[35]:

q = "SELECT DISTINCT artist_id FROM songs"
res = conn.execute(q)
all_artist_ids = list(map(lambda x: x[0], res.fetchall()))
conn.close()


# In[40]:

for k in range(4):
    print(all_artist_ids[k])


# In[41]:

files_per_artist = {}

for aid in all_artist_ids:
    files_per_artist[aid] = 0


# In[46]:

def func_to_count_artist_id(filename):
    h5 = GETTERS.open_h5_file_read(filename)
    artist_id = GETTERS.get_artist_id(h5)
    #print(artist_id)
    files_per_artist[artist_id] += 1
    h5.close()


# In[47]:

apply_to_all_files(msd_subset_data_path, func=func_to_count_artist_id)


# In[ ]:



