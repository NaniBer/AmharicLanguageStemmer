import collections
import glob


files = glob.glob(
    'C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Books/Indexes/*.txt')
indexList = []
for file in files:
    with open(file, 'r', encoding="utf-8") as f:
        try:
            data = f.read()
        except UnicodeDecodeError:
            f = open(file, 'r', encoding="utf-16")
            data = f.read()

        indexList.append(data.split())


df = {}
for i in range(len(indexList)):
    tokens = indexList[i]
    for w in tokens:
        try:
            df[w].add(i)
        except:
            df[w] = {i}


for i in df:
    df[i] = len(df[i])


attribute = dir(df)
print(df.values())
