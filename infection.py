# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Dean Anderson, Paanery Shah, Hayley Jarjoura, Madelynn Mills (no absences) Team #7 (Team Rick)
# Section:     503
# Assignment:  TEAM PROJECT
# Date:        3 December 2018

from Person import *
from random import *


def spread(subject, contacted, people):
    """
    The spread functions makes people sisck if the disease gets spread to them
    :param subject: the sick person that contacted all these people
    :param contacted: list of people that were contacted by the sick person
    :param people: list of all the people
    :return: returns nothing, just changed values of objects
    """
    closeCount = subject.getClose()
    # looping through people contacted by the sick person
    for i in range(len(contacted)):
        # This adds to transmission later
        transAdd = 0
        # If there are still people withing close contact to the sick person add 25% chance to the transmission percent
        if closeCount > 0:
            transAdd += 25
        # chance to compare to the percent chances
        chance = randint(0,100)
        # if there's a 75% chance of transmission, 75% of numbers between 0-100 are below 75, so if the number is below
        # 75, the chance happened
        if chance < subject.getTransmission() + transAdd:
            # same with this, but resistance is % chance you wont get sick, so its an opposite relationship
            if chance > people[contacted[i]].getResistance():
                # If the person isn't immune
                if not people[contacted[i]].isImmune():
                    # making the person sick if all of these conditions are met
                    people[contacted[i]].setSick(True)
                    subject.setNumSpread(subject.getNumSpread()+1)
        # 1 less number of people in close contact to the sick person
        closeCount -= 1

def peopleContacted(subject, people):
    """
    The peopleContacted function creates a list of people contacteed by a person
    :param subject: the sick person
    :param people: list of all the people
    :return: returns a alist of contacted people
    """
    contactList = []
    # looping through the number of people the person contacts
    for i in range(subject.getActivity()):
        # random person
        randomNum = randint(0, len(people) - 1)
        # If the person is in the contactList, it picks a new person
        while randomNum in contactList:
            randomNum = randint(0, len(people) - 1)
        # adding the person to the list of contacted people
        contactList.append(randomNum)
    # returning the list
    return contactList