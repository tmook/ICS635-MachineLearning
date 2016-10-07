#/usr/bin/python
import numpy as np

class GaussianData:
   def __init__(self, fileName=None):
      #init all member variables
      self.DataSet = []
      self.ClusterDataSet = []
      self.trueCenters = []
      self.totalClusters = 0
      self.totalDataPoints = []
      if fileName != None:
         importDataSet(fileName)


   ##### ** THE DISTANCE PARAMETER will generated a center point from the PREVIOUSLY CREATED CENTER POINT **** ####
   ## This will generate a cluster and add it to the dataset. This function will add 1 cluster per function call.
   ## e.g. if you call this function 5 times, you will have 5 clusters in your data set
   def generateCluster(self, data_size=10, distance=-1, center=None, hscale=1, vscale=1):
      #why do i have to initialize again?!
      if not center:
         center = []
      #generate center point based on distance from previous clusters center
      if distance > -1:
         #generate random rad
         a = np.random.uniform(0,2*np.pi)
         #store x coordiate
         center.append( self.trueCenters[self.totalClusters-1][0] + distance * np.cos(a) )
         #store y coordiate
         center.append( self.trueCenters[self.totalClusters-1][1] + distance * np.sin(a) )
      #generate random center if center is empty
      if not center:
         #get x
         center.append(np.random.randint(-10, 10))
         #get y
         center.append(np.random.randint(-10, 10))
      #generate data
      cov = [[1*hscale, 0], [0, 1*vscale]]
      generatedSet = np.random.multivariate_normal(center, cov, np.int(data_size)).tolist()

      #add generated data to ClusterDataSet
      self.ClusterDataSet.append(list(generatedSet))
      #add generated data to DataSet
      for point in generatedSet:
         self.DataSet.append(list(point))
      #store center point
      self.trueCenters.append(list(center))
      #increment number of clusters
      self.totalClusters += 1
      #update data points for this cluster
      self.totalDataPoints.append(data_size)

   ## This function will generate a cluser but not add it to the dataset,
   ## the data does not get saved in the object so you will have to save
   ## the return value to access the data again.
   def generateSingleCluster(self, data_size=10, distance=-1, center=None, hscale=1, vscale=1):
      #why do i have to initialize again?!
      if not center:
         center = []
      #generate center point based on distance from previous clusters center
      if distance > -1:
         #generate random rad
         a = np.random.uniform(0,2*np.pi)
         #store x coordiate
         center.append( self.trueCenters[self.totalClusters-1][0] + distance * np.cos(a) )
         #store y coordiate
         center.append( self.trueCenters[self.totalClusters-1][1] + distance * np.sin(a) )
      #generate random center if center is empty
      if not center:
         #get x
         center.append(np.random.randint(-10, 10))
         #get y
         center.append(np.random.randint(-10, 10))
      #generate data
      cov = [[1*hscale, 0], [0, 1*vscale]]
      return np.random.multivariate_normal(center, cov, np.int(data_size)).tolist()


   def getDataSet(self):
      return list(self.DataSet)


   def getClusterDataSet(self):
      return list(self.ClusterDataSet)


   def getTotalClusters(self):
      return self.totalClusters


   def getTrueCenters(self):
      return list(self.trueCenters)


   def getTotalDataPoints(self):
      return len(self.DataSet)


   def getInfo(self):
      print "Total number of Clusters: "+str(self.getTotalClusters())
      print "Total number of data points: "+str(self.getTotalDataPoints())
      print ""
      for idx, center in enumerate(self.trueCenters):
         print "Cluster: "+str(idx+1)
         print "number of data points: "+str(self.totalDataPoints[idx])
         print "Centered at: "+str(center)
         print ""


   ## this function clears the dataset
   def clearAll(self):
      self.DataSet = []
      self.ClusterDataSet = []
      self.trueCenters = []
      self.totalClusters = 0
      self.totalDataPoints = []
         

   def ImportData(self, filename=None):
      if filename == None:
         print "provide file name for importData"
      else:
         pass


   def ExportData(self, filename=None):
      if filename == None:
         print "provide file name for ExportData"
      else:
         pass





###### Run this test of this script is main
if __name__ == "__main__":
   gd = GaussianData()
   gd.generateCluster()
   print gd.getDataSet()
   gd.getInfo()
   
   print "------------"
   gd = GaussianData()
   gd.generateCluster()
   gd.getInfo()
   gd.generateCluster()
   gd.getInfo()

   print "------------"
   gd = GaussianData()
   gd.generateCluster()
   gd.generateCluster()
   gd.generateCluster(center=[5,5])
   print gd.generateSingleCluster(center=[10,10])
   gd.generateCluster()
   gd.generateCluster()
   gd.getInfo()
   print gd.getTrueCenters()

   print "------------"
   gd = GaussianData()
   gd.generateCluster()
   gd.generateCluster(data_size=5, distance=3)
   gd.getInfo()
   print gd.getTrueCenters()
