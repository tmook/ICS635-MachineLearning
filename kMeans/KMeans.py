#/usr/bin/python

# input dataset is of x and y coordinates in a list, as a list (e.g. [ [1,2], [2,1], [-1,-2], [1,-2] ] )
# default values of k=2 and maxIter=300
# output is a list of labels of which corresponging xy values it belongs to.
import random


class kMeans:
   def __init__(self, k=2, maxIter=300):
      #init all member variables
      self.K = k
      self.maxIterations = maxIter
      self.InitialIterations = maxIter
      self.Centroids = []
      self.labels = []


   ##set k
   def setK(self, k):
      self.K = k


   ##set max iterations
   def setMaxIterations(self, maxIter):
      self.maxIterations = maxIter
      self.InitialIterations = maxIter


   ##get labels
   def getLabels(self):
      return list(self.labels)


   ##get centroids
   def getCentroids(self):
      return list(self.Centroids)


   ##get total iterations to convergence
   def getTotalIterations(self):
      return self.InitialIterations - self.maxIterations


   ##randomly choose k points in data set as initial centroids
   def randInitCentroids(self, dataset):
      for i in range(0,self.K):
         self.Centroids.append(random.choice(dataset))
   

   ##find euclidean distance between two points
   def euclideanDist(self, pointA, pointB):
      return ( (pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2 )**0.5


   ##compares each element in list, if equal return true else return false
   def cmpListEqual(self, listA, listB):
      #check list size first
      if(len(listA) != self.K) or (len(listB) != self.K):
         return False
         
      #check each element in the list
      for i in range(0,self.K):
         if(listA[i][0] != listB[i][0]):
            return False
         if(listA[i][1] != listB[i][1]):
            return False

      #lists are equal
      return True
   

   ## apply labels to points
   def fit(self, data=[], centroids=[]):
      #initialize/reset  labels, max iterations, converged, dataSet, and initial centroids
      self.Centroids = []
      self.labels = []
      self.maxIterations = self.InitialIterations
      converged = False
      dataSet = list(data)
      if (len(centroids) != self.K):
         if (len(centroids) > 0):
            print "WARNING: initial number of centroids does not match K clusters, randomizing centroids"
         self.randInitCentroids(dataSet)
      else:
         self.Centroids = list(centroids)

      while (self.maxIterations > 0) and (not converged):
         currentLabels = []
         #for each point in dataset
         for point in dataSet:
            minDist = -1
            label = 0
            #for each centroid
            for l, c in enumerate(self.Centroids):
               #calculate euclidian distance
               curDist = self.euclideanDist(c,point)
               #if current disntace is < prev centroid distance
               if (minDist < 0) or (curDist < minDist):
                  #update new label
                  label = l
                  #update min distance
                  minDist = curDist
            #append label to label list
            currentLabels.append(label)
         #store current_labels to output label list
         self.labels = list(currentLabels)

         ## update centroids
         #initialize label count to zeros
         newCentroids = [ [0.0,0.0] for i in range(0,self.K) ]
         labelCount = [0] * self.K 
         for idx, lbl in enumerate(self.labels):
            #calculate new average for x of centroid at label[idx]
            newCentroids[lbl][0] = ((newCentroids[lbl][0] * labelCount[lbl]) + dataSet[idx][0]) / (labelCount[lbl]+1)
            #calculate new average for y at label[idx]
            newCentroids[lbl][1] = ((newCentroids[lbl][1] * labelCount[lbl]) + dataSet[idx][1]) / (labelCount[lbl]+1)
            #update labelCount
            labelCount[lbl] += 1
         
         #check for convergence 
         converged = self.cmpListEqual( self.Centroids, newCentroids)
         #update centroids
         self.Centroids = list(newCentroids) 
         #update maxIterations
         self.maxIterations -= 1

      #return labels 
      return list(self.labels)


   ##Create plot of results
   def plotResults(self, data=[], filename=None, trueCentroids=[], show=False):
      import matplotlib
      matplotlib.use('TkAgg')
      import matplotlib.pyplot as pyplot

      pyplot.figure(1)
      colorNorm = pyplot.matplotlib.colors.Normalize(vmin=0, vmax=self.K)
      colorMap = pyplot.matplotlib.cm.gist_rainbow

      #plot data set with o as marker
      for i in range(0,len(data)):
         #pyplot.plot(data[i][0],data[i][1],color=colors[self.labels[i]],marker="o",)
         sc = pyplot.scatter(data[i][0],data[i][1],s=45,c=self.labels[i]+1,cmap=colorMap,norm=colorNorm,marker="o",)
      #plot centroids with daimond as marker
      pyplot.scatter(self.Centroids[0][0],self.Centroids[0][1],color="green",marker="d",s=128, label="Final Centroids")
      for i in range(1,len(self.Centroids)):
         pyplot.scatter(self.Centroids[i][0],self.Centroids[i][1],color="green",marker="d",s=128)
      #plot true centroids with * as marker
      if len(trueCentroids) > 0:
         pyplot.scatter(trueCentroids[0][0],trueCentroids[0][1],color="black",marker="*",s=128,label="True Centroids")
         for i in range(1,len(self.Centroids)):
            pyplot.scatter(trueCentroids[i][0],trueCentroids[i][1],color="black",marker="*",s=128)

      pyplot.title("Converged in "+str(self.getTotalIterations())+" iterations")
      pyplot.legend(loc='best')
      pyplot.colorbar(sc, ticks=range(1,self.K+1), label="Cluster")
      #pyplot.grid(True, which='both')

      if filename != None:
         pyplot.savefig(filename+".png",bbox_inchex='tight')
         print "Figure saved to file '"+filename+".png'"
      if show:
         pyplot.show()
      #clear figure
      pyplot.clf()





###### Run this test of this script is main
if __name__ == "__main__":
   #tests
   data = [ [-5,-5],[5,5],[-4,-5],[-6,-5],[-5,-4],[-5,-6],[6,5],[4,5],[5,4],[5,6] ]
   km = kMeans(2, 300)
   km.fit(data)
   km.fit(data)
   #km.plotResults(data)
   #raw_input('press return to continue')
   #km.plotResults(data,"test1")
   #raw_input('press return to continue')
   #km.plotResults(data,show=True)
   #raw_input('press return to continue')
   #km.plotResults(data,filename="test2", show=True)
   #raw_input('press return to continue')

   data = [ [-5,-5],[5,5],[-4,-5],[-6,-5],[-5,-4],[-5,-6],[6,5],[4,5],[5,4],[5,6] ,[-5,5], [-4,5],[-6,5],[-5,4],[-5,6],[5,-5],[4,-5],[6,-5],[5,-4],[5,-6]]
   km = kMeans(4, 300)
   output = km.fit(data, centroids=[[-5.0, -5.0], [5.0, 5.0], [5.0, -5.0], [-5.0, 5.0]])
   #km.plotResults(data,show=True)
   centroids = km.getCentroids()
   print centroids

   km.setK(2)
   output = km.fit(data, centroids=[[-5.0, -5.0], [5.0, 5.0], [5.0, -5.0], [-5.0, 5.0]])
   
   km.setK(4)
   output = km.fit(data)
   print km.getTotalIterations()

   output = km.fit(data)
   labl = km.getLabels()
   for idx,e in enumerate(output):
      if e != labl[idx]:
         print "getLabel and output of fit wrong"

   km.setMaxIterations(3)
   output = km.fit(data)
   if km.getTotalIterations() != 3:
      print "sometime wrong with iterations check (could also picked THE centroids on randomization)", km.getTotalIterations()
   
   km.setMaxIterations(300)
   km.setK(2)
   print km.fit(data)
   km.setK(4)
   print km.fit(data)

