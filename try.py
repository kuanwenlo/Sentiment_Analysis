import glob
from sys import argv
from stemming.porter2 import stem
import nltk
import dictionary as dic
from nltk.corpus import stopwords
import svm
from svmutil import *
import feature


dictionary = dic.makeDict();

neg_files = glob.glob("neg/*.txt")
pos_files = glob.glob("pos/*.txt")
neg_test = glob.glob("test_neg/*.txt")
pos_test = glob.glob("test_pos/*.txt")


trainingTexts = []
trainingTarget = []
trainingData = []
test_texts = []
test_target = []
test_data = []

for f in neg_files:
	data = open(f, "r")
	text = data.read()
	trainingTexts.append(text)
	trainingTarget.append(-1)
for f in pos_files:
	data = open(f, "r")
	text = data.read()
	trainingTexts.append(text)
	trainingTarget.append(1)
for f in neg_test:
	data = open(f, "r")
	text = data.read()
	test_texts.append(text)
	test_target.append(-1)
for f in pos_test:
	data = open(f, "r")
	text = data.read()
	test_texts.append(text)
	test_target.append(1)

for text in trainingTexts:
	trainingDatum = feature.featureSelect(text, dictionary)
	trainingData.append(trainingDatum)
for text in test_texts:
	test_datum = feature.featureSelect(text, dictionary)
	test_data.append(test_datum)
	#print test_datum

m = svm_train(trainingTarget, trainingData)

#test_target = [-1, 1]
#test_input = [[3, 1, 3, 15, 19, 20, 21, 25, 14, 18], [30, 30, 40, 45, 24, 20, 21, 25, 14, 18]]
p_labels, p_acc, p_vals = svm_predict(test_target, test_data, m)


print p_labels