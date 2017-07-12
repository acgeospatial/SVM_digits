print "starting"
print "------"
### Delete following 2 lines if not interested in time to run code
import time
time_start = time.time()
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

### Delete following line if not interested in time to run code
print "time to import libraries: ", time.time() - time_start
print "------"
### Delete following line if not interested in time to run code
time_start2 = time.time()
### Number of training samples to not train on, but test
not_train_no = 10
##' load the data
digits = datasets.load_digits()
### set the classifier
clf = svm.SVC()
clf = svm.SVC(gamma=0.001, C=100)
### assign the data and target
X,y = digits.data[:-not_train_no], digits.target[:-not_train_no]
### classify
clf.fit(X,y)

for i in range(1,(not_train_no +1)):
	### Loop through the not trained data and make a prediction using SVM
	print "SVM predicts this number: ", clf.predict(digits.data[[-i]])
	### Strings for the figure header
	Pred = str(clf.predict(digits.data[[-i]]))
	Actual = str(digits.target[-i])
	figureHead = "Prediction: " + Pred + " Labelled as: " + Actual
	### Delete following line if not interested in time to run code
	print "time to train data set, run SVM and make prediction: ", time.time() - time_start2
	### create the plot and set the figure title to prediction and labelled
	fig = plt.figure(1)
	fig.canvas.set_window_title(figureHead)
	plt.imshow(digits.images[-i], cmap=plt.cm.gray_r, interpolation='nearest')
	plt.show()
	### save figure?
	### savefig('/.png')
