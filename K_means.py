import math
import numpy as np
from sys import argv
from random import shuffle, choice, randrange
import matplotlib.pyplot as plt

#preprocessing step
class K_means:
    def __init__(self,file_name = 'points.txt', K = 2):
        # a list of provided data points
        self.data = []
        # a list of assigned clusters
        self.assigned_clusters = []
        # a list of distances of points from each cluster center
        self.dist_from_centers = []
        # a list of the cluster centers
        self.cluster_centers  = []
        # the name of the input file
        self.filename = file_name
        # the number of clusters required
        self.K = np.int(K)
        # number of data points whose cluster was changed in an iteration
        self.number_of_changes = len(self.data)
        # number of iterations
        self.iteration = 0
        # maximum number of permitted iterations to avoid infinite loop
        self.MAX_ITERATIONS = 10
        # calling pre-process
        self.preprocess_data()
        # initiating cluster centers
        self.initial_centers()
        # finding initial distances
        self.calc_euclidean_distances()
        # initial assignment of clusters
        self.assign_cluster()

    # function for pre-processing the data for the model
    def preprocess_data(self):
        # creating a list of available data points
        with open(self.filename) as f:
            for line in f:
                item = line.split(' ')
                for i in range(len(item)):
                    item[i] = np.float(item[i])
                self.data.append(item)
        shuffle(self.data)

    # function for calculating euclidean distance for a pair of data point and a cluster center
    def euclidean_distance(self, data_point, cluster_center):
        sum_of_squared_differences = 0
        for i in range(len(data_point)):
            sum_of_squared_differences += math.pow((data_point[i] - cluster_center[i]),2)
        return math.sqrt(sum_of_squared_differences)

    # function to calulate the euclidean distance of each data point from each cluster center
    def calc_euclidean_distances(self):
        for i in range(len(self.data)):
            dist = []
            for j in range(self.K):
                dist.append(self.euclidean_distance(self.data[i], self.cluster_centers[j]))
            self.dist_from_centers.append(dist)

    # function to assign clusters to the data points
    def assign_cluster(self):
        for i in range(len(self.data)):
            cluster = self.dist_from_centers[i].index(min(self.dist_from_centers[i]))
            if self.iteration == 0:
                self.assigned_clusters.append([cluster, self.cluster_centers[cluster]])
            else:
                if(self.assigned_clusters[i][0] != cluster):
                    self.number_of_changes += 1
                self.assigned_clusters[i] = [cluster, self.cluster_centers[cluster]]


    # function to find initial cluster centers
    def initial_centers(self):
        for i in range(self.K):
            self.cluster_centers.append(choice(self.data))

    # function to update the position of cluster center once and update the assignment of clusters and the distances respectively
    def update_center(self):
        self.iteration += 1
        self.number_of_changes = 0;
        for j in range(self.K):
            s =[0]*len(self.data[0])
            c = 0;
            for i in range(len(self.data)):
                if self.assigned_clusters[i][0] == j:
                    for n in range(len(s)):
                        s[n] += self.data[i][n]
                    c += 1
            for n in range(len(self.cluster_centers[j])):
                if c > 0:
                    self.cluster_centers[j][n] = s[n]/c
        self.assign_cluster()
        self.calc_euclidean_distances()



    '''
    # function to update assigned clusters
    def assign_cluster(self):
        for i in range(len(self.data)):
            cluster = self.dist_from_centers[i].index(min(self.dist_from_centers[i]))
            self.assigned_clusters[i] = [cluster, self.cluster_centers[cluster]]
    '''


# main
# initializing the model (handles : data pre-processing and initial assignment of clusters)
'''
model = K_means()
for i in range(len(model.data)):
    print (model.assigned_clusters[i])
model.update_center()
print((model.iteration, model.number_of_changes, model.cluster_centers))

'''

model = K_means(argv[1], argv[2])

print((model.iteration, model.number_of_changes, model.cluster_centers))


for i in range(model.MAX_ITERATIONS):
    #if (model.number_of_changes > 0):
    model.update_center()
    print((model.iteration, model.number_of_changes, model.cluster_centers))

f= open("output.txt","w+")
for i in range(len(model.cluster_centers)):
    for j in range(len(model.cluster_centers[i])):
        # writing the final values for cluster centers rounded off to 9 decimal places
        f.write(''.join(str(round(model.cluster_centers[i][j], 9))))
        f.write(' ')
    f.write('\n')







