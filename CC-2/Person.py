import math
import cv2

class Person:

    def __init__(self, centroid, max_path):

        # determine box centroid
        self.centroid = centroid

        # add centroid to path
        self.path = []
        self.path.append(self.centroid)

        # path limit
        self.max_path = max_path
    
    # determine euclidean distance to new point is within tolerance
    def compare(self, new_centroid):   
        if self.centroid != None:
            dist = math.hypot(self.centroid[0] - new_centroid[0], self.centroid[1] - new_centroid[1])
            if dist <= 25:
                return True
        return False
    
    # update centroid and path
    def update(self, new_centroid):
        self.centroid = new_centroid
        self.path.append(self.centroid)
        if len(self.path) > self.max_path:
            self.path.pop(0)
    
    # determine person is out of frame when path is all null values
    def isValid(self):
        if len(self.path)==self.max_path and len(set(self.path)) == 1 and set(self.path).pop() == None:
            return False
        return True