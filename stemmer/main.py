import stemmerMain
import writersNames
import tf
import idf

# sentence = input("ቃላትን ያስገቡ፡ ")
sentence = "የተደረሰ በይስማዕከ መጽሐፎች"
words = sentence.split()
queryList = []
len = len(words)
i = 0
values = {}
sorted_dict = {}
while (i < len):
    word = words[i]
    if (word not in writersNames.writers[0]):
        word = stemmerMain.stemmerMain(word)
        queryList.append(word)
        if (word in writersNames.writers[0]):
            for item in writersNames.writers:
                if (i < len-2):
                    if (words[i+1] in item[1]):
                        queryList.append(words[i+1])
                        i = i+1
                    else:
                        continue

    i = i+1

tfValues = tf.calculateTf(queryList)
idfValues = idf.calculateIdf()
for word in queryList:
    if (word in idfValues and word in tfValues):
        values[word] = (idfValues[word])*(tfValues[word])

    else:
        values[word] = 0
    sorted_dict = {k: v for k, v in sorted(
        values.items(), key=lambda item: item[1])}
print(sorted_dict)
