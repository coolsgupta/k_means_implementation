import math
import numpy as np
from sys import argv
from random import shuffle, choice, randrange
import matplotlib.pyplot as plt

#preprocessing step
class K_means:
    def __init__(self,file_name = 'points_3.txt', K = 2):
        self.data = []
        self.assigned_clusters = []
        self.dist_from_centers = []
        self.cluster_centers  = []
        self.filename = file_name
        self.K = K
        self.preprocess_data()

    def preprocess_data(self):
        # creating a list of available data points
        with open(self.filename) as f:
            for line in f:
                item = line.split(' ')
                for i in range(len(item)):
                    item[i] = np.float(item[i])
                self.data.append(item)
        shuffle(self.data)

    def euclidean_distance(self, data_point, cluster_center):
        sum_of_squared_differences = 0
        for i in range(len(data_point)):
            sum_of_squared_differences += math.pow((data_point[i] - cluster_center[i]),2)
        return math.sqrt(sum_of_squared_differences)

    def calc_euclidean_distances(self):
        for i in range(len(self.data)):
            dist = []
            for j in range(self.K):
                dist.append(self.euclidean_distance(self.data[i], self.cluster_centers[j]))
            self.dist_from_centers.append(dist)

    def assign_cluster(self):
        for i in range(len(self.data)):
            cluster = np.argmin(self.dist_from_centers)
            self.assigned_clusters.append([cluster, self.cluster_centers[cluster]])



    def initial_centers(self):
        for i in range(self.K):
            self.cluster_centers.append(choice(self.data))

    def update_center(self):
        x


# main

x = K_means()
x.preprocess_data()
x.initial_centers()
x.calc_euclidean_distances()
x.assign_cluster()
for i in range(49):
    print (x.data[i])
    print (x.dist_from_centers[i])
    print(x.assigned_clusters[i][0])


