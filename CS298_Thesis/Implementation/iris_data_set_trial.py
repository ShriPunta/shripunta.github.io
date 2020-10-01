# Using the scikit learn inbuilt dataset of iris


from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


#Get data set
iris_dataset = datasets.load_iris()
print("-iris-features->",iris.feature_names)

print("-iris-data.top5->",iris.data[0:5])


#Use Panda to create a dataframe

pd_data=pd.DataFrame({
    'sepal len':iris.data[:,0],
    'sepal wid':iris.data[:,1],
    'petal len':iris.data[:,2],
    'petal wid':iris.data[:,3],
    'species':iris.target
})

print("-->",pd_data)


#Map features to labels
X=data[['sepal len', 'sepal wid', 'petal len', 'petal wid']]  
y=data['species']  

# train_test_split returns a tuple of 4 params. We split the data set into 25% test data and remaining training data
X_to_train, X_to_test, y_to_train, y_to_test = train_test_split(X, y, test_size=0.25)


print("-X_to_train->",X_to_train)
print("-X_to_test->",X_to_test)
print("-y_to_train->",y_to_train)
print("-y_to_test->",y_to_test)

classifierr=RandomForestClassifier(n_estimators=100)

classifierr.fit(X_to_train, y_to_train)

y_prediction = classifierr.predict(X_to_test)



# See the accuracy
print("Accuracy:",metrics.accuracy_score(y_to_test, y_prediction))


#Test Predict | sepal length, sepeal width, petal length, petal width
classifierr.predict([[4, 3, 2, 3]])
