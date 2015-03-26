from sys import argv
from stemming.porter2 import stem
import nltk
import dictionary as dic
from nltk.corpus import stopwords
import svm
from svmutil import *
dictionary = argv[1]
data = argv[2]



f1 = open(dictionary, 'r')
f2 = open(data,'r')

dictionary = dic.makeDict(f1);
text = f2.read();

stop = stopwords.words('english')
posNoun = 0
posVerb = 0
posAdj = 0
posAdv = 0
posAny = 0
negNoun = 0
negVerb = 0
negAdj = 0
negAdv = 0
negAny = 0 

filtered_words = [w for w in text.split() if not w in stop]
#print stop



for w in filtered_words:
	if(dictionary.get(w) == None):
		continue
	else:
		print w 
		fact = dictionary.get(w)
		if fact[0] == "weaksubj" :
			amp = 1
		elif fact[0] == "strongsubj" :
			amp = 3
		if fact[4] == "positive" :
			if fact[2] == "noun" :
				posNoun += amp
			elif fact[2] == "verb" :
				posVerb += amp
			elif fact[2] == "adj" :
				posAdj += amp
			elif fact[2] == "adverb" :
				posAdv += amp
			elif fact[2] == "anypos":
				posAny += amp
		elif fact[4] == "negative" :
			if fact[2] == "noun" :
				negNoun += amp
			elif fact[2] == "verb" :
				negVerb += amp
			elif fact[2] == "adj" :
				negAdj += amp
			elif fact[2] == "adverb" :
				negAdv += amp
			elif fact[2] == "anypos":
				negAny += amp

trainingData = (posNoun, posVerb, posAdj, posAdv, posAny, negNoun, negVerb, negAdj, negAdv, negAny)

print trainingData

#y = (-1, 1, 1, -1)

#x = ([8, 19, 13, 0, 13, 20, 18, 23, 1, 16], [40, 30, 29, 17, 28, 20, 18, 23, 1, 16], [70, 19, 20, 14, 17, 60, 18, 23, 1, 16], [8, 19, 13, 0, 13, 20, 18, 23, 1, 16])


#model = svm_train(y, x)



