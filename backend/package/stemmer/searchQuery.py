

import numpy as np
import ast
from filecmp import cmp
import glob
import json
import os
import pickle


def searchQuery(query):

    files = glob.glob(
        'C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Books/Indexes/Final Index/*.txt')
    foundDocuments = []
    for file in files:
        file_name = os.path.basename(file)
        file_name = file_name[:-4]
        with open(file, 'r', encoding="utf-16") as f:
            try:
                data = f.read()
            except UnicodeEncodeError:
                f = open(file, 'r', encoding="utf-16")
                data = f.read()
            data = ast.literal_eval(data)
            doc = list(data.keys())
            words = np.array(doc)

            wordCount = {}

            amount = {}

            length = len(query)
            threshold = length/4
            for word in query:
                if word in words:
                    term_count = (words == word).sum()
                    amount[word] = term_count
            if len(amount) >= threshold:
                foundDocuments.append(file_name)
            else:
                continue

    return foundDocuments
