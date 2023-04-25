import glob
import stemmerMain
import writersNames
import os
import letterDefinitions
import writersNames

# def RemoveStopWord():
# print("enter a sentence ")
# text = input()
# texts = text.split()


def addFiles(indexes, file_name):
    file_path = f"C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Books/Indexes/{file_name} index.txt"
    with open(file_path, 'w', encoding="utf-16") as file:
        file.write(' '.join(finalIndex))


index = []
finalIndex = []

files = glob.glob(
    'C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Books/utf-8/*.txt')

file_name = os.path.basename(files[0])
file_name = file_name[:-4]
# print(file_name)

for file in files:

    file_name = os.path.basename(file)
    file_name = file_name[:-4]

    with open(file, 'r', encoding="utf-8") as f:
        finalIndex.clear()
        index.clear()
        print(finalIndex)
        print("new file opened")
        data = f.read()
        print(file_name)

        texts = data.split()
        word = texts[0]
        # word = word[1:]
        index.append(word)
        size = len(texts)
        i = 1

        while (i < size):
            word = texts[i]
            if (len(word) > 1):
                if (word[-1] == "።" or word[-1] == ":" or word[-1] == "፣" or word[-1] == "፤"):
                    word = word[:-1]
                if (word[0] == "፣"):
                    continue
            elif (word == "፣"):
                i = i+1
                continue
            elif (len(word) == 1):
                i = i+1
                continue
            if word not in letterDefinitions.StopWords:
                index.append(word)
            i = i+1

        for word in index:
            if (word in writersNames.writers):
                finalIndex.append(word)
            else:
                word = stemmerMain.stemmerMain(word)
                finalIndex.append(word)

    f.close()
    addFiles(finalIndex, file_name)


# f = open("C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Authors/ሀብታሙ አለባቸው.txt", "r", encoding="utf8")
# a = f.read()
# f.close

# texts = a.split()
# word = texts[0]
# word = word[1:]
# index.append(word)
# print(index)
# len = len(texts)
# i = 1


# while (i < len):
#     word = texts[i]
#     if word not in StopWords:
#         index.append(word)

#     i = i+1

# print(index)

# for word in index:
#     if (word[0] == "“"):
#         finalIndex.append(word)
#     elif (word[-1] == "”"):
#         finalIndex.append(word)
#     else:
#         word = stemmerMain.stemmerMain(word)
#         finalIndex.append(word)


# print(finalIndex)

# file_path = f"C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Authors/ኃይሉ ገብረዮሐንስ index.txt"
# with open(file_path, 'x', encoding="utf-8") as file:
#     file.write(' '.join(finalIndex))
