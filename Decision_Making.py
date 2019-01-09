from sklearn import tree 

values = []

#[height,weight,shoe size]
X = [[181,80,40], [177,70,43], [160,60,38], [154,54,37],
     [186,65,40], [190,90,47], [175,64,39], [177,70,40],
     [179,55,37], [171,75,42], [181,85,43]]

Y = ['male','female','female','female','male','male','male','female','male','female','male']

print('Enter height, weight and shoe size : ')
for i in range(3) :
	val = input()
	values.append(int(val))

clf = tree.DecisionTreeClassifier()

#fit method trains decision tree on data set
clf = clf.fit(X,Y)

prediction = clf.predict([values])
print(prediction)

