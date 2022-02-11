#This exercise is for create a gender classifier using the "sci-kit learn" library
import sklearn

from sklearn import tree

#[height, weigth, shoe size]

X = [[181,81,40], [160,70,38],[190,89,41],[187,69,42],[165,60,39],[150,59,36]]
Y = ["men","women","women","women","men","men"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

prediction = clf.predict([[160,70,38]])

print(prediction)