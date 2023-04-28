import stemmerMain
import writersNames
import searchQuery
import ranking


def main():

    # newQuery = input("ቃላትን ያስገቡ፡ ")
    sentence = "የተደረሰ በይስማዕከ ወርቂ መጽሕፍ"

    sentence2 = "ሀብታሙ አለባቸው"
    sentence3 = "ስለኢትዮጵያ ፖለቲካ ሀገር"
    # yewesdal menged yametal menged
    sentence4 = "የመጀመሪያ ልብወለድ መፅሐፍ"
    # tobia
    sentence5 = "የአዳም ረታ መጽሐፎች"
    # chegag ena tel
    sentence6 = "ስለኤርትራ መጽሐፍ"
    sentence7 = "ስለአገር ቋናቋ ጥናት"
    # ሃብታሙ አለባቸው

    sentence8 = "አጫጭር ልቦለድ አዳም"
    # ሕማማትና በገና by አዳም ረታ
    sentence9 = "እመጓ መፅሐፍ"
    sentence10 = "ማስታወሻ"
    # የፍሬሿ ማስታወሻ by ሄርሜላ ሰለሞን
    # ማስታወሻ

    sentence11 = "ግጥም"
    # የብርሃን ልክፍት

    # sentence = "የተደረሰ በይስማዕከ መጽሐፎች"
    # sentence2 = "ሀብታሙ"

    words = sentence.split()

    queryList = []
    length = len(words)

    i = 0
    values = {}
    sorted_dict = {}
    while (i < length):
        word = words[i]
        if (word not in writersNames.writers[0]):
            word = stemmerMain.stemmerMain(word)
            queryList.append(word)
        if (word in writersNames.writers[0]):
            queryList.append(word)
            for item in writersNames.writers:
                if (i < length-2):
                    if (words[i+1] in item[1]):
                        queryList.append(words[i+1])
                        i = i+1
                    else:
                        continue

        i = i+1

    relatedBooks = searchQuery.searchQuery(queryList)
    if (len(relatedBooks) == 0):
        print("No results found. Please add terms for a better results")
    rankedBooks = ranking.ranking(queryList, relatedBooks)
    rankedBooks = list(rankedBooks.keys())
    for books in rankedBooks:
        print(books)
    return rankedBooks


main()
