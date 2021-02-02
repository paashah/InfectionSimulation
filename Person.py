# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Dean Anderson, Paanery Shah, Hayley Jarjoura, Madelynn Mills (no absences) Team #7 (Team Rick)
# Section:     503
# Assignment:  TEAM PROJECT
# Date:        3 December 2018

class Person:
    def __init__(self, resistance, recovery, activity, closeCont, transmission):
        self.resistance = resistance
        self.recovery = recovery
        self.activity = activity
        self.close = (activity * closeCont/100)//1
        self.transmission = transmission
        self.sick = False
        self.immune = False
        self.numSpread = 0

    def getResistance(self):
        return self.resistance

    def getRecovery(self):
        return self.recovery

    def getActivity(self):
        return self.activity

    def getClose(self):
        return self.close

    def getTransmission(self):
        return self.transmission

    def getNumSpread(self):
        return self.numSpread

    def isSick(self):
        return self.sick

    def isImmune(self):
        return self.immune

    def setResistance(self,resistance):
        self.resistance = resistance

    def setRecovery(self,recovery):
        self.recovery = recovery

    def setActivity(self,activity):
        self.activity = activity

    def setClose(self,closeCont):
        self.close = closeCont

    def setTransmission(self,transmission):
        self.transmission = transmission

    def setNumSpread(self, numSpread):
        self.numSpread = numSpread

    def setSick(self,sick):
        self.sick = sick

    def setImmune(self,immune):
        self.immune = immune

    def __str__(self):
        return ("%d, %d, %d, %d, %d" % (self.resistance,self.recovery,self.activity,self.close,self.transmission))