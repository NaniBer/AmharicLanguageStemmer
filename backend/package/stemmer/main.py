
from .writersNames import writers
from .searchQuery import searchQuery
from .ranking import ranking
from .stemmerMain import stemmerMain


def main(query):
    # sentence = "የተደረሰ በይስማዕከ መጽሐፎች"
    # sentence2 = "ሀብታሙ"

    words = query.split()
    queryList = []
    length = len(words)
    i = 0
    values = {}
    sorted_dict = {}
    while (i < length):
        word = words[i]
        if (word not in writers[0]):
            word = stemmerMain(word)
            queryList.append(word)
            if (word in writers[0]):
                for item in writers:
                    if (i < length-2):
                        if (words[i+1] in item[1]):
                            queryList.append(words[i+1])
                            i = i+1
                        else:
                            continue

        i = i+1
    relatedBooks = searchQuery(queryList)
    rankedBooks = ranking(queryList, relatedBooks)
    return rankedBooks
