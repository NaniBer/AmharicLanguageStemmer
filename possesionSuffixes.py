import letterDefinitions

def PossessionSuffixes(word):

  lastword = word[-1] 
  lastthreewords= word[-3:]

  if lastword in letterDefinitions.possesionWords1:
    word= word[:1] 

  elif lastthreewords in letterDefinitions.possesionWords2:
    word= word[:-3]


  elif lastword in letterDefinitions.secondLetter :
      index= letterDefinitions.secondLetter.index(word[-1])
      word= word.replace(word[-1], letterDefinitions.sixthLetter[index] )

  elif lastword in letterDefinitions.fifthLetter:
        index1= letterDefinitions.fifthLetter.index(word[-1])
        word= word.replace(word[-1], letterDefinitions.sixthLetter[index1])

  return word

      
 

 

