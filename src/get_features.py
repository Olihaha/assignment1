#i did this in python originally but due to the 4-5ish mins it took my pc to run the script i put it into a notebook because then i could make sure it was going and didnt crash
import spacy
import os
import csv
import re

# Load the en_core_web_md model from spaCy
nlp = spacy.load("en_core_web_md")

# Input and output directories
input_dir = "in/USEcorpus/"
output_dir = "out"

# Looping through the subdirectories in the input folder
for subdir in os.listdir(input_dir):
    # creating empty list to store results in each subdirectory
    results = [] 
    # path to current directory
    subdir_path = os.path.join(input_dir, subdir)
    for filename in os.listdir(subdir_path):
        file_path = os.path.join(subdir_path, filename)
        with open(file_path, "r", encoding="latin-1") as f:
            text = f.read() 
        text = re.sub(r"<.*?>", "", text) # Removing random tags.
        # process the text using spacy model
        doc = nlp(text) 
        #getting number of tokens
        num_tokens = len(doc) 
        #number of words
        num_words = len([token for token in doc if token.is_alpha])
        #freq of nouns, verbs, adjectives and adverbs
        freq_nouns = sum([token.pos_ == "NOUN" for token in doc]) / num_words * 10000
        freq_verbs = sum([token.pos_ == "VERB" for token in doc]) / num_words * 10000
        freq_adjs = sum([token.pos_ == "ADJ" for token in doc]) / num_words * 10000
        freq_advs = sum([token.pos_ == "ADV" for token in doc]) / num_words * 10000
        #number of unique persons locations and organisations
        unique_per = len(set([ent.text for ent in doc.ents if ent.label_ == "PER"]))
        unique_loc = len(set([ent.text for ent in doc.ents if ent.label_ == "LOC"]))
        unique_org = len(set([ent.text for ent in doc.ents if ent.label_ == "ORG"]))
        #adding results
        results.append([filename, freq_nouns, freq_verbs, freq_adjs, freq_advs, unique_per, unique_loc, unique_org])
        #write the results to a csv file
    with open(os.path.join(output_dir, f"{subdir}.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Filename", "RelFreq NOUN", "RelFreq VERB", "RelFreq ADJ", "RelFreq ADV", "Unique PER", "Unique LOC", "Unique ORG"])
        writer.writerows(results)