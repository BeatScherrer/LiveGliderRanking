# -*- coding: utf-8 -*-

class Competitor:
    """
    Competitor class.
    
    Defines a competitor with information needed for calculations and display.
    """
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

