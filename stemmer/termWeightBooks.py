import re
import tf
import idf
import os
import glob
import json


def termWeight():
    files = glob.glob(
        'C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Books/Indexes/*.txt')
    idfValues = idf.calculateIdf()
    tfidf = []
    for file in files:
        file_name = os.path.basename(file)
        file_name = file_name[:-10]
        if 'b' in file_name:
            i = (file_name.index('b'))
            bookTitle = file_name[:i]
            author = file_name[i+3:]

        else:
            bookTitle = file_name
            author = ""

        tfValues = {}
        termWeights = {}
        values = {}
        fileTerm = {}
        with open(file, 'r', encoding="utf-8") as f:
            try:
                data = f.read()
            except UnicodeDecodeError:
                f = open(file, 'r', encoding="utf-16")
                data = f.read()
            words = data.split()
            for word in bookTitle:
                words.append(word)
            authors = author.split()
            for word in authors:
                words.append(word)
            # print(file_name)
            tfValues = tf.calculateTf(words)
            for word in words:
                values[word] = (idfValues[word])*(tfValues[word])
            sorted_dict = {k: v for k, v in sorted(
                values.items(), key=lambda item: item[1])}
            # print(sorted_dict)
            tfidf = list(sorted_dict.values())
            length = len(tfidf)
            q1 = round(1/4*(length+1))-1
            q2 = round(3/4 * (length+1))-1
            # print(q1, q2)
            indexes = list(sorted_dict)
            indexTerm = []
            while (q2 > q1):
                indexTerm.append(indexes[q1])
                q1 = q1+1

                value = sorted_dict[indexes[q1]]
                fileTerm[indexes[q1]] = value
            biggestValue = sorted_dict[indexes[q2]]
            title = bookTitle.split()
            for word in title:
                fileTerm[word] = biggestValue
            authors = author.split()
            for word in authors:
                fileTerm[word] = biggestValue

            # file_path = f"C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Books/Indexes/Final Index/{file_name}.txt"
            # with open(file_path, 'w', encoding="utf-16") as file:
            #     file.write(str(fileTerm))


termWeight()
