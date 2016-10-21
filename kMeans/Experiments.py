#!/usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot
import numpy as np

from KMeans import kMeans
from GaussianData import GaussianData


###############################################
### Experiment 1                            ###
### plot of k-means with 5 clusters         ###
###  each cluster with 100 data points each ###
###############################################
def Experiment1():
   gd = GaussianData()
   gd.generateCluster(data_size=100)
   gd.generateCluster(data_size=100)
   gd.generateCluster(data_size=100)
   gd.generateCluster(data_size=100)
   gd.generateCluster(data_size=100)

   data = gd.getDataSet()
   km = kMeans(5)
   km.fit(data)
   trueClusterPoints = gd.getClusterDataSet()
   resultClusterPoints = km.getLabelPoints(data)
   ## get Accuracy of results
   totalMissClassPoints = 0
   for rCP in resultClusterPoints:
      minErrors = -1
      for trueCP in trueClusterPoints:
         currentErrors = 0
         for truePoint in trueCP:
            if truePoint not in rCP:
               currentErrors +=1
         if (minErrors < 0) or (currentErrors < minErrors):
            minErrors = currentErrors
      totalMissClassPoints += minErrors
   accuracy = float(totalMissClassPoints) / gd.getTotalDataPoints()
   ##accuracy
   print 100 - 100*accuracy
   km.plotResults(data,trueCentroids=gd.getTrueCenters(),filename="experiment1",show=True)


###############################################
### Experiment 2                            ###
### Error meansure based on summed distance ###
###############################################
def Experiment2():
   error = [100]
   gd = GaussianData()
   gd.generateCluster(data_size=100)
   gd.generateCluster(data_size=100)
   gd.generateCluster(data_size=100)
   gd.generateCluster(data_size=100)
   gd.generateCluster(data_size=100)

   data = gd.getDataSet()
   km = kMeans(5, 1)
   #find percentage canged first time
   labels = km.fit(data)
   centroids = km.getCentroids()
   distanceSum = 0
   iterations = 1
   #sum up all the distances from the point to its nearest centroid
   for idx, lbl in enumerate(labels):
      distanceSum += km.euclideanDist(centroids[lbl],data[idx])
   error.append((distanceSum/len(data))**2)
   percent_change = np.abs((error[iterations-1]-error[iterations]) / error[iterations-1])
   #run through while loop till percentage change is < 0.001
   while (iterations <  500) and (percent_change > 0.001):
      labels = km.fit(data,centroids)
      centroids = km.getCentroids()
      distanceSum = 0
      iterations +=1
      #sum up all the distances from the data point to its nearest centroid
      for idx, lbl in enumerate(labels):
         distanceSum += km.euclideanDist(centroids[lbl],data[idx])
      error.append((distanceSum/len(data))**2)
      percent_change = np.abs((error[iterations-1]-error[iterations]) / error[iterations-1])

   km.plotResults(data,trueCentroids=gd.getTrueCenters(),filename="experiment2a")
   # Create plot
   pyplot.clf()
   pyplot.figure(1)
   pyplot.plot(np.arange(iterations),error[1:])
   pyplot.title('error vs. iteration')
   pyplot.ylabel('error')
   pyplot.axis('tight')
   pyplot.xlabel('iteration')
   pyplot.savefig("experiment2b.png",bbox_inchex='tight')
   print "Figure saved to file 'experiment2b.png'"
   #pyplot.show()






### uncomment a test to run Experiements ###
Experiment1()
#Experiment2()









