import csv
import numpy as np
from sklearn import datasets

def main():
  #Load dataset
  wine = datasets.load_wine()
  
  print('Data:', wine.data[0:5])
  print('Target', wine.target[0:5])
  
  dtata_X = wine.data[:, np.newaxis, 0]
  dtata_Y = wine.data[:, np.newaxis, 1]
  
  print(wine.feature_names[0], dtata_X[0:5])
  print(wine.feature_names[1], dtata_Y[0:5])
  
  for i in range(0, 12, 2):
    m = i
    n = (m+1) % 12
    dtata_X = wine.data[:, np.newaxis, m]
    dtata_Y = wine.data[:, np.newaxis, n]
    
    print('m:', m)
    print('n:', n)
    
    print(wine.feature_names[m])
    print(wine.feature_names[n])
  
    filename = (wine.feature_names[m] + '__' + wine.feature_names[n] + '.csv').replace('/', '-')
    
    print(filename)
    write_csv(filename, dtata_X, dtata_Y, wine.target)
    print('-----------')

  return

def write_csv(filename, X, Y, T):
  with open(filename, mode='w+') as csv_file:
    fieldnames = ['X', 'Y', 'T']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    for i in range(len(X)):
      writer.writerow({'X': (' %5.5f' % X[i]), 'Y': (' %5.5f' % Y[i]), 'T': (' %d' % T[i])})


main()

#gnuplot graph.gp


