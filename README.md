# Assignement 1 -  Extracting linguistic features using spaCy

---
# Introduction and contents
This repository contains a Python script named "get_features.py" designed for information extraction tasks such as part-of-speech (PoS) tagging and named-entity recognition (NER). The script calculates the relative frequency of Nouns, Verbs, Adjectives, and Adverbs per 10,000 words, as well as the total count of unique persons (PER), locations (LOC), and organizations (ORG). The extracted information

## data
The project utilizes the “Uppsala Student English Corpus” which consists of 1,489 essays composed by 440 Swedish university students studying English at varying levels. The essays are organized into 14 sub-folders within the "USEcorpus" folder, with each sub-folder representing different terms, styles, and subjects of the essays.

## models 
The information extraction process employs the en_core_web_md SpaCy model for Python. This pre-trained model, of medium size, is well-suited for various English natural language processing (NLP) tasks.
I've added the installation of this model to the setup script.

## script functions
The Python script follow a structured pipeline with the following steps:
1. import the necessary libraries and loads the spacy model
2. iterats over each subdirectory in the input directory and creates an empty list to store the analysis results.
3. it reads every file within the subdirectoy removing random tags using regular expressions and processes it using the spacy model.
4. it then calculates the information and requested for the task. 
5. then saves the csv files in an out folder for every subdirectory.

## how to replicate
### copy the repository 
git clone https://github.com/AU-CDS/assignment-1---linguistic-analysis-using-nlp-Olihaha

make sure to be in correct directory
(cd assignment-1)

### scripts
Run either setup.sh followed up by run.sh or setupandrun.sh

setup.sh activates a virtual environment, pip installs necessary libraries and deactives.

run.sh activates the virtual environment, runs the script and deactives itself again.

runandsetup.sh does both.


