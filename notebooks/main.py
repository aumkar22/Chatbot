
# coding: utf-8

# In[1]:


import nltk
import time
import re
import settings


# In[ ]:


h5 = settings.apply_to_all_files()

#print(h5)
# In[ ]:


def posTagSentence(inStr):
    text = nltk.word_tokenize(inStr.lower())
    return nltk.pos_tag(text)


# In[ ]:


def nerTagSentence(tagList):
    return (nltk.ne_chunk(tagList, binary=True))


# In[ ]:


def findSongToArtistQuery(taggedStr):
    #Regex for finding artist of a song
    exStA = re.compile('((who.*)?((sang|made|sings)|(is.*(artist|singer|band).*(of|from|for))|((what|which).*)?(artist|SINGER|band) ?(sang|made|of)?))')
    #Regex for finding songs of an artist
    exAtS = re.compile('(((what.*)|(which.*))?((song)s?.*?of.*?)|((song)s?.*?(did)))')
    exFSA = re.compile('((what.*))?(famous|popular|((hit)s?))')
    foundStA = re.search(exStA, taggedStr)
    foundAtS = re.search(exAtS, taggedStr)
    foundFSA = re.search(exFSA, taggedStr)
    if foundStA is not None:
        sta = re.sub(r'([^\w\s]|[A-Z])', '',taggedStr[foundStA.span()[1]:]).lstrip().rstrip().title()
        #print(a)
        sta1 = bytes(sta, encoding = 'ascii')
        for i in range(len(h5)):
            f = settings.GETTERS.open_h5_file_read(h5[i])
            if settings.GETTERS.get_title(f) == sta1:
                found_artist = settings.GETTERS.get_artist_name(f).decode("utf-8")
                f.close()
                return print("The artist you are looking for is: ", found_artist)
                break
            else:
                f.close()
        return print("Artist not found")
    elif foundAtS is not None:
        ats = re.sub(r'((did|write|sing|make)|[^\w\s]|[A-Z])', '',taggedStr[foundAtS.span()[1]:]).lstrip().rstrip().title()
        ats1 = bytes(ats, encoding = 'ascii')
        #print(s1)
        for i in range(len(h5)):
            f = settings.GETTERS.open_h5_file_read(h5[i])
            #print(f)
            if settings.GETTERS.get_artist_name(f) == ats1:
                found_song = settings.GETTERS.get_title(f).decode("utf-8")
                f.close()
                return print("One of their songs is: ", found_song)
                break
            else:
                f.close()
        return print("Song not found")
    elif foundFSA is not None:
        fsa = re.sub(r'((by|(song)s?)|[^\w\s]|[A-Z])', '',taggedStr[foundFSA.span()[1]:]).lstrip().rstrip().title()
        #print(a)
        fsa1 = bytes(fsa, encoding = 'ascii')
        for i in range(len(h5)):
            f = settings.GETTERS.open_h5_file_read(h5[i])
            if settings.GETTERS.get_artist_name(f) == fsa1:
                song_hotness, famous_song = settings.GETTERS.get_song_hotttnesss(f)
                famous_song = famous_song.decode("utf-8")
                f.close()
                return print("The famous song by the artist is: ", famous_song)
                break
            else:
                f.close()
        return print("Artist not found")
    else:
        return print("Query not understood")


# In[ ]:


#Hi and Hello are currently recognised as NNP's
def initialiseChat():
    print("Hi, I am RiffGetter. You can ask anything that has to do with music!")
    time.sleep(.3)
    inStr = posTagSentence(str(input()))
    print ("What would you like to know?")
    continueChat()


# In[ ]:


def continueChat():
    while True:
        inStr = str(input())
        if exitCheck(inStr.lower()):
            print("Very well, goodbye, nice talking to you!")
            break
        elif posCheck(inStr.lower()):
            print("What would you like to know?")
        else:
            posTagged = posTagSentence(inStr)
            nerTagged = nerTagSentence(posTagged)
            parse_string = ' '.join(str(nerTagged).split())
            findSongToArtistQuery(parse_string)
            print("Is there anything else I can help you with?")


# In[ ]:


def exitCheck(inStr):
    negatives = ["no", "nope", "no thanks", "bye", "no,", "nope,"]
    for neg in negatives:
        if inStr.startswith(neg):
            return True
    return False

def posCheck(inStr):
    positives = ["yes", "yup", "yus", "yeah", "ja", "okay", "ok"]
    for pos in positives:
        if inStr.startswith(pos):
            return True
    return False

# In[ ]:


if __name__ == "__main__":
    initialiseChat()

