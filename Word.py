#import Debug file for Word class
from Debug import DEBUG
from Location import Location

#Word class
class Word(Location):
#Deleted Grid within the class Word parameters for now

    #Orientations stored in a list through a class variable called ORIENTATIONS
    ORIENTATIONS = ["HR", "HL", "VD", "VU", "DRD", "DRU", "DLD", "DLU"]
    
    #The constructor which takes a word, an orientation, and a location as parameters
    def __init__(self, word, orientation=None, location=None):
        self.word = word.upper()
        self.orientation = orientation
        self.location = location
    def __lt__(self, other): #https://www.geeksforgeeks.org/operator-overloading-in-python/
        if self.word < other.word:
            return False
        else:
            return True
        
    #Getters and setters for the instance variables _word, _orientation, and _location
    @property 
    def word(self): 
        return self._word
    @word.setter
    def word(self, word):
        self._word = word.upper()
    @property 
    def orientation(self): 
        return self._orientation
    @orientation.setter
    def orientation(self, orientation):
        self._orientation = orientation
    @property 
    def location(self): 
        return self._location
    @location.setter
    def location(self, location):
        self._location = location
    
    #A __str__() method that returns a string representation of the Word in two formats
    def __str__(self):
        if DEBUG == False:
            return self.word.upper()
        else:
            return ("{}/{}@{}".format(self.word, self.orientation, self.location))
