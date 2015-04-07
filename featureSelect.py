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

#stop = stopwords.words('english') 
stop = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']
print stop
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

filtered_lines = [w for w in text.split('.')]
#print stop
#print filtered_line[0]
#print stop

negTag = ["isn't", "aren't", "hasn't", "haven't", "don't", "doesn't","ain't", "aint", "won't", "couldn't", "cannot", "can't", "not", "no", "neither", "nor", "shouldn't", "wouldn't"]
print negTag
#filtered_words = [w for w in text.split() if not w in stop]

for line in filtered_lines:
	filtered_words = [w for w in line.split() if not w in stop]
	neg = False
	for w in filtered_words:
		if w in negTag:
			neg = True
		if(dictionary.get(w) == None):
			continue
		else:
			#print w 
			fact = dictionary.get(w)
			if fact[0] == "weaksubj" :
				amp = 1
			elif fact[0] == "strongsubj" :
				amp = 3
			if (fact[4] == "positive" and neg == False) or ((fact[4] =='negative') and neg):
				
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
			elif (fact[4] == "negative" and neg == False) or ((fact[4]=='positive') and neg ):
				
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
	
"""
for w in filtered_words:
	if(dictionary.get(w) == None):
		continue
	else:
		#print w 
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
"""

trainingData = (posNoun, posVerb, posAdj, posAdv, posAny, negNoun, negVerb, negAdj, negAdv, negAny)

print trainingData

#y = (-1, 1, 1, -1)

#x = ([8, 19, 13, 0, 13, 20, 18, 23, 1, 16], [40, 30, 29, 17, 28, 20, 18, 23, 1, 16], [70, 19, 20, 14, 17, 60, 18, 23, 1, 16], [8, 19, 13, 0, 13, 20, 18, 23, 1, 16])


#model = svm_train(y, x)




