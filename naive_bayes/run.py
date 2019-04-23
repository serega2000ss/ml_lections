import csv
import numpy as np
from sklearn import datasets, metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

def main():
  #Load dataset
  wine = datasets.load_wine()
  
  print("Features: ", wine.feature_names)
  print("Labels: ", wine.target_names)
  print("Data Shape: ", wine.data.shape)
  print(wine.data[0:5])
  print(wine.target)
  
  # Split dataset into training set and test set
  X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3,random_state=109) # 70% training and 30% test
  
  #Create a Gaussian Classifier
  gnb = GaussianNB()
  
  #Train the model using the training sets
  gnb.fit(X_train, y_train)
  
  print('predicting ----------')
  #Predict the response for test dataset
  y_pred = gnb.predict(X_test)
  print(X_test[0:5])
  print(y_pred)
  
  # Model Accuracy, how often is the classifier correct?
  print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
  
  return

main()
