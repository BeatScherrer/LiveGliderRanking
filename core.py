# -*- coding: utf-8 -*-

from haversine import Haversine

class Competitor:
    # Constructor
    def __init__(self, name, callsign, plane):
        self.name = name
        self.callsign = callsign
        self.plane = plane
        self.task_started = False
        self.task_started_at = None
        
    # Define representation.
    def __repr__(self):
        return self.callsign

class Task:
    '''
    Task class. Initalization with the task type ("AAT/Race") and a list of
    task points and assigns the corresponding distances.
    '''
    def __init__(self, task_type, task_points):
        self.task_type = task_type
        self.task_points = task_points
        self.task_distance = 0
        if(task_type == "Race"):
            for i in range(0, len(task_points)-1):
                self.task_distance += Haversine(task_points[i], task_points[i+1]).km
                
    def __repr__(self):
        return self.task_type + " Task: " + str(round(self.task_distance, 3)) + "km"


# Lat Lon Point
class Point:
    # Constructor
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
    def __repr__(self):
        return '(' + str(self.lat) + ',' + str(self.lon) + ')'

# TaskPoint class. Hold the type of sector.
class TaskPoint(Point):
    def __init__(self, lat, lon, radius):
        Point.__init__(self, lat, lon)
        self.radius = radius
    
    def __repr__(self):
        return '(' + str(self.lat) + ', ' + str(self.lon) + ') radius: ' + str(self.radius)
        
if __name__ == '__main__':
    # Define pilots
    pilot1 = Competitor("Beat Scherrer", "XY", "ASH-26E")
    pilot2 = Competitor("John Doe", "XX", "LS-4")
    
    competitors = [pilot1, pilot2]
    
    # Define Task
    point1 = TaskPoint(47.439063, 7.490152, 5)
    point2 = TaskPoint(47.417701, 7.500470, 5)
    point3 = TaskPoint(47.394342, 7.545052, 5)
    point4 = TaskPoint(47.439063, 7.490152, 5)
    task = Task("Race", [point1, point2, point3, point4])
    
    print(task.task_points[1])
    print(task)

    