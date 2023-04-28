import ast
import os

import numpy as np
import tf
import idf


def ranking(queryList, documents):
    values = {}
    cosineValue = {}
    sorted_cosine = {}
    sorted_dict = {}
    relationshipWithTheQuery = {}
    tfValues = tf.calculateTf(queryList)
    idfValues = idf.calculateIdf()
    for word in queryList:
        if (word in idfValues and word in tfValues):
            values[word] = (idfValues[word])*(tfValues[word])
        else:
            values[word] = 0
    sorted_dict = {k: v for k, v in sorted(
        values.items(), key=lambda item: item[1])}
    queryTfIDF = np.array(list(sorted_dict.values()))
    for doc in documents:
        file_path = f"C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Books/Indexes/Final Index/{doc}.txt"
        docArr = []
        with open(file_path, 'r', encoding="utf-8") as f:
            file_name = os.path.basename(file_path)
            file_name = file_name[:-4]
            try:
                data = f.read()
            except UnicodeDecodeError:
                f = open(file_path, 'r', encoding="utf-16")
                data = f.read()
            data = ast.literal_eval(data)
            for words in queryList:
                if (words in data):
                    docArr.append(data[words])
                else:
                    docArr.append(0)
            dot = np.dot(queryTfIDF, docArr)
            cosineValue[file_name] = dot
            sorted_cosine = dict(
                sorted(cosineValue.items(), key=lambda item: item[1], reverse=True))
    return sorted_cosine
