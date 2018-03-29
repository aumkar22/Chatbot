# Chatbot

The **Name** Chatbot is a Python based Music domain chatbot which can be interacted with via Command line. The data set used for answering the queries by Chatbot is the freely available Million Song Dataset which is a collection of audio features and metadata for a million contemporary popular music tracks. For this project, we use a subset of the data set provided at https://tinyurl.com/yb2xu3av. The subset is a collection of 10000 songs randomly sampled from the main data set.

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

The script can then be run as:

```
python main.py
```

## Goal and Approach

The goal of the chatbot is to do basic interactions and answer some of the basic questions asked, for example, 'Who is the artist of the song Immigrant Song?'

The Chatbot works by searching 
