# Lloyds algorithm
# Implementation of Kmeans Lloyds algorithm
# made to complete Rosalind programming problem, so it takes a specific format
# input: data dimensions and datapoints
# output: k centroids of clusters determined from input data

import random
import math
import numpy as np
from matplotlib import pyplot as plt

def lloyd(k, m, data):
	"returns set of k centers for the clusters in given m-dimensional data"
	#choose random points as centroids
	centroids = list()
	clusters = list(0 for i in range(len(data))) #links each node to a cluster by index value
	for i in range(k): #initialize centroid points as the first k nodes in data
		#pos = round(random.random() * len(data))
		centroids.append(list(x for x in data[i]))
	Converged = False
	plotGraph(data, centroids=centroids)
	while not Converged:
		for i in range(len(data)): #assign nodes to nearest centroid
			best_centroid = -1
			best_dist = 9000
			for c in range(len(centroids)):
				d = euclidean(data[i], centroids[c])
				if best_dist == -1: #no centroid assigned yet
					best_centroid = c
					best_dist = d
				else:
					if d < best_dist:
						best_centroid = c
						best_dist = d
			clusters[i] = best_centroid #assigns index value of centroid (index from centroids)
		movedCentroid = False
		#place centroids in their centers of mass
		for i in range(len(centroids)):
			cluster = list() #gets nodes that belong to this cluster
			for j in range(len(clusters)):
				if clusters[j] == i:
					cluster.append(data[j]) #adds the node's coord values
			#get average values of each m dimensions
			newCentroid = centerOfGravity(cluster)
			for val in range(len(newCentroid)):
				if newCentroid[val] != centroids[i][val]: #checks if centroid moved
					movedCentroid = True
			#plotCluster(data, centroids[i], cluster)
			centroids[i] = newCentroid
		if not movedCentroid: #if no centroids change, they have converged
			Converged = True
	plotGraph(data, centroids=centroids)
	#print(centroids)
	return centroids

def centerOfGravity(cluster):
	"returns centroid CoG for given cluster"
	m = len(cluster[0]) #gets number of dimensions of data
	mValues = np.zeros(m)
	for i in range(len(cluster)):
		for j in range(m):
			mValues[j] += cluster[i][j]
	output = mValues / len(cluster)
	return output

def plotGraph(data, centroids=None):
	"plots the given data coordinates on a graph (only works on 2-D)"
	X = [row[0] for row in data]
	Y = [row[1] for row in data]
	plt.scatter(X,Y,color='blue')
	if centroids != None:
		cX = [row[0] for row in centroids]
		cY = [row[1] for row in centroids]
		plt.scatter(cX,cY,color='red')
	plt.show()

def plotCluster(data, centroid, cluster):
	"shows the nodes in the cluster of the given centroid"
	X = [row[0] for row in data]
	Y = [row[1] for row in data]
	plt.scatter(X,Y,color='blue')
	cX = [row[0] for row in cluster]
	cY = [row[1] for row in cluster]
	plt.scatter(cX, cY, color='green')
	plt.scatter(centroid[0], centroid[1], color='red')
	plt.show()

def euclidean(a, b):
	"gives euclidean distance for the given nodes"
	n = len(a)
	d = 0
	for i in range(n):
		d = d + ((a[i] - b[i]) ** 2)
	return math.sqrt(d)

def readRosalind(file):
	"opens rosalind input from input.txt"
	with open(file, 'r') as f:
		lines = f.readlines()
	k = 0
	m = 0
	data = list()
	for i in range(len(lines)):
		if i == 0:
			k = int(lines[i].split(" ")[0])
			m = int(lines[i].split(" ")[1])
		else:
			data.append(list(float(i) for i in lines[i].split(" ")))
	return (k, m, data)

file = 'input.txt'
rosalind = readRosalind(file)
kmeans = lloyd(rosalind[0], rosalind[1], rosalind[2])
#print(kmeans)

#plotGraph(rosalind[2])
for ans in kmeans:
	s = ""
	for a in ans:
		s = s + str(round(a, 3)) + " "
	print(s)