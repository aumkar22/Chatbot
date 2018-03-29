
# coding: utf-8

# In[1]:


import nltk
import time
import re
import os
import sys
import time
import glob
import numpy as np
import settings


# In[ ]:


h5 = settings.apply_to_all_files()


# In[ ]:


ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ADD_DATA_DIR = os.path.join(ROOT_DIR, 'AdditionalFiles')
SUBSET_FILE = os.path.join(ADD_DATA_DIR, 'subset_msd_summary_file.h5')
MSD_CODE_PATH = os.path.join(ROOT_DIR, 'MSongsDB')
sys.path.append(os.path.join(MSD_CODE_PATH, 'PythonSrc'))


# In[ ]:


import hdf5_getters as GETTERS


# In[2]:


def posTagSentence(inStr):
    text = nltk.word_tokenize(inStr.lower())
    return nltk.pos_tag(text)


# In[3]:


def nerTagSentence(tagList):
    for el in range(0, len(tagList)):
        if tagList[el][1] in ('JJ') or tagList[el][1] in ('NN'):
            newTuple = (tagList[el][0].upper(), tagList[el][1])
            tagList[el] = newTuple
    return nltk.ne_chunk(tagList, binary = True)


# In[4]:


#Use this one to keep strings lowercase
def nerTagSentence2(tagList):
    return (nltk.ne_chunk(tagList, binary=True))


# In[5]:


def stripTags(inStr):
    ex1 = re.sub(r'[^\w]', ' ', s)


# In[15]:


def findSongToArtistQuery(taggedStr):
    ex1 = re.compile('((who.*)?((sang|made)|(is.*(artist|singer|band).*of))|                     ((what|which).*)?(artist|SINGER|band) ?(sang|made|of)?)')
    found = re.search(ex1, taggedStr)
    print(found)
    if found is not None:
#         print(taggedStr)
#         print(found.span())
#         print(taggedStr[found.span()[1]:])
        a = re.sub(r'([^\w\s]|[A-Z])', '',taggedStr[found.span()[1]:]).lstrip().rstrip()
        for i in range(len(h5)):
            if GETTERS.get_artist_name(h5[i]) is a:
                print("Artist found!")
                return True
            else:
                print("Artist not found")
                return False
    else:
        print("Query not understood")
        return False
    


# In[16]:


text = "Which artist sang bohemian rhapsody?"
posTagged = posTagSentence(text)
nerTagged = nerTagSentence2(posTagged)
print("POS-TAGGED: ", posTagged, "\n")
parse_string = ' '.join(str(nerTagged).split())
print("NER-TAGGED: ", parse_string, "\n")
print("Found query: ", findSongToArtistQuery(parse_string))


# In[8]:


#Hi and Hello are currently recognised as NNP's
def initialiseChat():
    print("Welcome to the music-chatbot. You can ask anything that has to do with music! Start your conversation by saying hello!")
    time.sleep(.3)
    inStr = posTagSentence(input())
    name = ""
    for el in range (0, len(inStr)):
        if inStr[el][1] == 'NNP':
            name = " " + inStr[el][0]
    print ("Hello" + name + ", What would you like to know?")
    continueChat()
    


# In[9]:


#exitCheck function should still be defined
def continueChat():
    while True:
        inStr = input()
        if exitCheck(inStr.lower()):
            print("Very well, I hope I could be of help.")
            break
        else:
            posTagged = posTagSentence(inStr)
            nerTagged = nerTagSentence2(posTagged)
            parse_string = ' '.join(str(nerTagged).split())
            print(findSongToArtistQuery(parse_string))
            print("Is there anything else I can help you with?")
        


# In[10]:


#Assumes inStr is already POS-tagged
#Returns the predicate of what the question is about
def detectQuestions(tagList):
    start = 0
    end = len(tagList)
    for el in range(0, len(tagList)):
        if tagList[el][1] == 'WP':
            start = el + 1
        if tagList[el][1] == '.' and tagList[el][0] == '?':
            end = el
    pred = tagList[start:end]
    return pred


# In[11]:


def exitCheck(inStr):
    negatives = ["no", "nope", "n", "no thanks", "bye"]
    if inStr in negatives:
        return True
    else:
        return False


# In[12]:


initialiseChat()

