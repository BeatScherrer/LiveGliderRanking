# -*- coding: utf-8 -*-

import numpy as np

from PyProj import Proj
from shapely.geometry import Point

from haversine import 


p1 = Proj(init='epsg:26915')

class Task:
    """
    Task class. Initalization with the task type ("AAT/Race") and a list of
    task points consisting of shapely polygons.
    """   
    def __init__(self, task_type, task_points):
        self.task_type = task_type
        self.task_points = task_points
        
        self.start_point = StartPoint(task_points[0])
        self.finnish_point = FinnishPoint(task_points[len(task_points)])
        
	self.task_distance = 0
	for i in range(0, len(task_points)):
	    self.task_distance += Haversine(task_points[i], task_points[i+1]).km 
        
	    #calculate AAT Distances?        
	    #task_min_distance = 0
	    #task_max_distance = 0
	    #for i in task_poi
    def __repr__(self):
        return self.task_type + " Task: " + str(round(self.task_distance, 3)) + "km"


# Lat Lon Point
class Point:
    """
    This class defines a point in a local euclidean coordinate system. 
    
    A point can be constructed using the spherical coordinates which are 
    projected using the projection defined in the global projection object 
    proj from the PyProj library.
    """
    # Constructor
    def __init__(self, lat, lon):
        self.vector = np.array([])
        self.lat = lat
        self.lon = lon
        self.x, self.y = p1(lat, lon)
        
    def __repr__(self):
        return '(' + str(self.lat) + ',' + str(self.lon) + ')'

class TaskPoint(Point):
    """
    A taskpoint consists of point and the corresponding shapely polygon.
    
    The point is represented in x,y coordinates while it is constructed using
    latitude and longitude.
    """
    def __init__(self, lat, lon, radius):
        
        x, y = p1(lat, lon)
        Point.__init__(self, x, y)
        
        self.radius = radius
    
    def __repr__(self):
        return '(' + str(self.lat) + ', ' + str(self.lon) + ') radius: ' + str(self.radius)
    
class StartPoint(Point):
    """
    This class defines a start point of a task.
    
    The start point consists of a line which needs to be passed in the correct
    direction to start the task and thus is a special task point.
    """
    def __init__(self, lat, lon, length=10):
        Point.__init__(self, lat, lon)
        self.length = length
        
    def __repr__(self):
        return repr(Point.__repr__(self)) + ' Line: ' + str(self.length) + ' km'
        

class FinishPoint(Point):
    def __init__(self, lat, lon, length=1):
        Point.__init__(self, lat, lon)
        self.length = 1
        
    def __repr__(self):
        return repr(Point.__repr__(self)) + ' Line: ' + str(self.length) + 'km'
        
if __name__ == '__main__':
    # Define Task
    start_point = StartPoint(47.439063, 7.490152, length=10)
    point1 = TaskPoint(47.439063, 7.490152, 5)
    point2 = TaskPoint(47.417701, 7.500470, 5)
    point3 = TaskPoint(47.394342, 7.545052, 5)
    point4 = TaskPoint(47.439063, 7.490152, 5)
    task = Task("Race", [point1, point2, point3, point4])
    
    print(task.task_points[1])
    print(task)
    
    start_point = StartPoint(1,2,10)
    print(start_point)
