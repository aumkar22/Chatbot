
# coding: utf-8

# In[ ]:


import nltk
import time
import re
import settings


# In[ ]:


h5 = settings.apply_to_all_files()


# In[ ]:


def posTagSentence(inStr):
    text = nltk.word_tokenize(inStr.lower())
    return nltk.pos_tag(text)


# In[ ]:


#Use this one to keep strings lowercase
def nerTagSentence(tagList):
    return (nltk.ne_chunk(tagList, binary=True))


# In[ ]:


def findSongToArtistQuery(taggedStr):
    #Regex for finding artist of a song
    exStA = re.compile('((who.*)?((sang|made|sings)|(is.*(artist|singer|band).*(of|from|for))|                     ((what|which).*)?(artist|SINGER|band) ?(sang|made|of)?))')
    #Regex for finding songs of an artist
    exAtS = re.compile('(((what.*)|(which.*))?((song)s?.*?of.*?)|((song)s?.*?(did)))')
    foundStA = re.search(exStA, taggedStr)
    foundAtS = re.search(exAtS, taggedStr)
    if foundStA is not None:
        a = re.sub(r'([^\w\s]|[A-Z])', '',taggedStr[found.span()[1]:]).lstrip().rstrip()
        for i in range(len(h5)):
            f = settings.GETTERS.open_h5_file_read(h5[i])
            if settings.GETTERS.get_title(f) is a:
                print("The artist you are looking for is: ", settings.GETTERS.get_song_name(f))
                return True
                f.close()
                break
            else:
                f.close()
                print("Artist not found")
                return False
    elif foundAtS is not None:
        s = re.sub(r'((did|write|sing|make)|[^\w\s]|[A-Z])', '',taggedStr[foundAtS.span()[1]:]).lstrip().rstrip()
        for i in range(len(h5)):
            f = settings.GETTERS.open_h5_file_read(h5[i])
            if settings.GETTERS.get_artist_name(f) is s:
                print("One of their songs is: ", settings.GETTERS.get_title(f))
                return True
                f.close()
                break
            else:
                f.close()
                print("Song not found")
                return False
    else:
        print("Query not understood")
        return False


# In[ ]:


# text = "What songs did Queen make?"
# posTagged = posTagSentence(text)
# nerTagged = nerTagSentence2(posTagged)
# parse_string = ' '.join(str(nerTagged).split())
# print("Found query: ", findSongToArtistQuery(parse_string))


# In[ ]:


#Hi and Hello are currently recognised as NNP's
def initialiseChat():
    print("Welcome to the ***name*** chatbot. You can ask your music related questions here. Try starting off by saying hello!")
    time.sleep(.3)
    inStr = posTagSentence(input())
    name = ""
    for el in range (0, len(inStr)):
        if inStr[el][1] == 'NNP':
            name = " " + inStr[el][0]
    print ("Hello" + name + ", What would you like to know?")
    continueChat()
    


# In[ ]:


def continueChat():
    while True:
        inStr = input()
        if exitCheck(inStr.lower()):
            print("Very well, I hope I could be of help.")
            break
        elif inStr.lower() is "yes":
            print("What would you like to know?")
        else:
            posTagged = posTagSentence(inStr)
            nerTagged = nerTagSentence(posTagged)
            parse_string = ' '.join(str(nerTagged).split())
            findSongToArtistQuery(parse_string)
            print("Is there anything else I can help you with?")
        


# In[ ]:


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


# In[ ]:


def exitCheck(inStr):
    negatives = ["no ", "nope ", "n", "no thanks", "bye"]
    for neg in negatives:
        if inStr.startswith(neg):
            return True
    return False


# In[ ]:


if __name__ == "__main__":
    initialiseChat()

