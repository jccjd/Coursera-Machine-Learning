from sklearn import svm
x = [[3,3],[4,3],[1,1]]
y = [1,1,-1]
model = svm.SVC(kernel='linear')
model.fit(x,y)


