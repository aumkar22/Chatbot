# Chatbot

The **RiffGetter** Chatbot is a Python based Music domain chatbot which can be interacted with via Command line. The data set used for answering the queries by Chatbot is the freely available Million Song Dataset which is a collection of audio features and metadata for a million contemporary popular music tracks. For this project, we use a subset of the data set provided at https://tinyurl.com/yb2xu3av. The subset is a collection of 10000 songs randomly sampled from the main data set.

The data set files provided are in HDF5 format and the project provides scripts to access these files via their Github repository: https://github.com/tbertinmahieux/MSongsDB. We use these files to access the subset to answer the queries asked to the Chatbot. For convenience, we have included the necessary scripts in our repository.

## Installation

Cloning the repository:

```
git clone https://github.com/aumkar22/Chatbot.git
```

## Running the Chatbot

In the command line, go to the path where the repository is cloned and access the **notebook** folder. For running python on Windows 7+ through Command line, Python should be added to the path. The steps to do this are described below:

```
1. Right-click My Computer --> Properties --> Advanced System settings
2. In the Advanced tab, click the 'Environment Variables' button
3. Edit Path and add the path till the 'notebook' folder of the repository and click OK.
```
For Python version 3.x 'tables' and 'pytables' modules needs to be installed. This can be done as:

```
conda install tables 

```
and 

```
conda install -c conda-forge pytables

```

The script can then be run as:

```
python main.py
```

## Goal and Approach

The goal of the chatbot is to do basic interactions and answer some of the basic questions asked, for example, 'Who is the artist of the song Immigrant Song?'

The Chatbot works by extracting a query from the input question using regular expressions. The query is then compared to one attribute of every file in the database, depending on the question. In the example 'Who is the artist of the song Immigrant Song?' the Chatbot will compare the substring 'Immigrant Song' to the song title for every file. When a match is found, the artist's name is returned as ouput on the command line. 

Currently there are two possible queries one might try. The first is to find the artist of a certain song, the second is to find a song by a given artist. The bot allows users to keep asking questions as long as needed. 

In detecting the type of query a small set of regular expressions is used. These expressions determine if the users wants to know an artist name or a song tile by looking at the structure of the sentence. The WH-question word and some keywords are taken into account to achieve this. The chatbot assumes the query is entered in proper english. When an expression is matched the string is pruned to only contain song or artist name, which allows it for cheap lookup in the database. This is necessary since iterating over all 10.000 songs once already takes a significant amount of time. 

## Query Examples
Examples of working queries:
![Working Example](https://github.com/aumkar22/Chatbot/blob/master/notebooks/Chatbot_example.PNG)

Examples where the RiffGetter fails:
![Fail Image](https://github.com/aumkar22/Chatbot/blob/master/notebooks/CB_fail_Image.PNG)
## Future Improvements

Ideally the Chatbot accesses the full Million Songs Database so it can answer as many queries as possible. The current available resources do not allow this to be done in a reasonable amount of time. With resources like external storage or a better GPU we will be able to provide more and more accurate answers. 

The query extraction is not very robust yet. Another improvement would be to either extend the set of regular expressions, or use different methods like Intention Analysis to extract the query of the user. With this it could also be possible to take things like spelling errors into account. 

Finally, it would be nice if the chatbot could handle more query types. Recommended artists or similar songs based on previous input would be a really nice addition for users that want to explore different kinds of music. 
