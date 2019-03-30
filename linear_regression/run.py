import csv
import numpy as np
from sklearn import datasets, linear_model

def main():
  # Load the diabetes dataset
  diabetes = datasets.load_diabetes()
  
  # Use only one feature
  diabetes_X = diabetes.data[:, np.newaxis, 2]
  
  # Split the data into training/testing sets
  diabetes_X_train = diabetes_X[:-20]
  diabetes_X_test = diabetes_X[-20:]
  
  # Split the targets into training/testing sets
  diabetes_y_train = diabetes.target[:-20]
  diabetes_y_test = diabetes.target[-20:]
  write_csv('diabets_2_train.csv', diabetes_X_train, diabetes_y_train)
  write_csv('diabets_2_test.csv', diabetes_X_test, diabetes_y_test)
  
  # Create linear regression object
  regr = linear_model.LinearRegression()
  
  # Train the model using the training sets
  regr.fit(diabetes_X_train, diabetes_y_train)
  
  # Make predictions using the testing set
  diabetes_y_pred = regr.predict(diabetes_X_test)
  write_csv('diabets_2_pred.csv', diabetes_X_test, diabetes_y_pred)
  
  print('Done!')
  return

def write_csv(filename, X, Y):
  with open(filename, mode='w') as csv_file:
    fieldnames = ['X', 'Y']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    for i in range(len(X)):
      writer.writerow({'X': (' %5.5f' % X[i]), 'Y': (' %5.5f' % Y[i])})

main()
