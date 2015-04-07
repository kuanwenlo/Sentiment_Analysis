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

raw_data = []
target_data = []
trainingData = []

for f in neg_files:
	data = open(f, "r")
	text = data.read()
	raw_data.append(text)
	target_data.append(-1)
for f in pos_files:
	data = open(f, "r")
	text = data.read()
	raw_data.append(text)
	target_data.append(1)

for text in raw_data:
	trainingDatum = feature.featureSelect(text, dictionary)
	trainingData.append(trainingDatum)
	

m = svm_train(target_data, trainingData)

test_target = [-1, 1]
test_input = [[3, 1, 3, 15, 19, 20, 21, 25, 14, 18], [30, 30, 40, 45, 24, 20, 21, 25, 14, 18]]
p_labels, p_acc, p_vals = svm_predict(target_data, trainingData, m)


#px.predict([3, 1, 3, 15, 19, 20, 21, 25, 14, 18])		

print p_labels