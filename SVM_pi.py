print "starting"
print "------"
import time
time_start = time.time()
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

print "time to import libraries: ", time.time() - time_start
print "------"

time_start2 = time.time()

not_train_no = 10

digits = datasets.load_digits()

clf = svm.SVC()

clf = svm.SVC(gamma=0.001, C=100)

X,y = digits.data[:-not_train_no], digits.target[:-not_train_no]

clf.fit(X,y)

for i in range(1,(not_train_no +1)):
	print i
	print "SVM predicts this number: ", clf.predict(digits.data[[-i]])
	Pred = str(clf.predict(digits.data[[-i]]))
	Actual = str(digits.target[-i])
	figureHead = "Prediction: " + Pred + " Labelled as: " + Actual
	#print "time to train data set, run SVM and make prediction: ", time.time() - time_start2
	fig = plt.figure(1)
	fig.canvas.set_window_title(figureHead)
	plt.imshow(digits.images[-i], cmap=plt.cm.gray_r, interpolation='nearest')
	plt.show()
