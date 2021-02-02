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
import infection
import matplotlib.pyplot as plt

people = []
numPeople = int(input('Enter the number of people as an integer in the test population'))

print('\nResistance Percent (recommended 10% - 90%): ')
# resistance is percent chance a person wont contract the disease
resLow = int(input("Enter the lowest percent resistance you want possible as an integer: "))
resHigh = int(input("Enter the highest percent resistance you want possible as an integer: "))
# recovery is the number of days it takes for a person to recover from the disease

print('\n',75*'-','\n\nRecovery Day (recommended 4 - 20): ')
recLow = int(input("Enter the lowest number of days to recover you want possible as an integer: "))
recHigh = int(input("Enter the highest number of days to recover you want possible as an integer: "))

print('\n',75*'-','\n\nContact Number (recommended 3 - 50): ')
# activity is the number of people a person contacts in a day
actLow = int(input("Enter the lowest number of people a person can contact in a day you want possible as an integer: "))
actHigh = int(input("Enter the highest number of people a person can contact in a day you want possible as an integer: "))

print('\n',75*'-','\n\nTransmission Percent (recommended 10% - 75%): ')
# transmission is the percent chance the disease will be transmitted to a person
transLow = int(input("Enter the lowest percent transmission you want possible as an integer: "))
transHigh = int(input("Enter the highest percent transmission you want possible as an integer: "))

print('\n',75*'-','\n\nClose Contact Percent (recommended 10% - 25%): ')
# close contact is the percent of people a person contacts that is considered close contact
closeLow = int(input("Enter the lowest percent of people a person contacts that will be considered close contact as an integer: "))
closeHigh = int(input("Enter the highest percent of people a person contacts that will be considered close contact as an integer: "))

# Loops through numPeople number of times, creating that many people
for n in range(numPeople):
    # Setting all the variables for the new object
    res = randint(resLow,resHigh)
    rec = randint(recLow,recHigh)
    act = randint(actLow,actHigh)
    trans = randint(transLow,transHigh)
    closeCont = randint(closeLow,closeHigh)
    # Creating a new person object and adding it to the list
    people.append(Person(res,rec,act,closeCont,trans))

# Calculating average recovery time over the initial population
avgRecovery = 0
for person in people:
    avgRecovery += person.getRecovery()
avgRecovery /= numPeople

# patient 0 is people[0]
people[0].setSick(True)
# Creating a list of the people the person contacted
contactList = infection.peopleContacted(people[0],people)

# Trying to spread the infection to people the person contacted
infection.spread(people[0], contactList, people)
# theSick is a a list of sick people
theSick = [people[0]]

# Adding people to the sick list if they're sick
for i in range(len(contactList)):
    if people[contactList[i]].isSick():
        theSick.append(people[contactList[i]])
# List of the number of sick people to plot the data at the end
listSickNum = [len(theSick)]
listImmuneNum = [0]
# Day 1
day = 1
# days is the list of day numbers that happened to plot the data at the end
days = [day]
# Printing the data in the console
print('day %d\nsick %d\nimmune %d\n' % (day, len(theSick), 0))

# Highest number of sick people throughout the simulation
mostSick = 0
# Looping until there are no more sick people
while len(theSick) > 0:
    immuneNum = 0
    contactList = []
    # looping through sick people on that day and spreading the sickness
    for sick in theSick:
        tempList = infection.peopleContacted(sick, people)
        infection.spread(sick, tempList, people)
        # Decreasing the recovery time because a day passed for the sick person
        sick.setRecovery(sick.getRecovery() - 1)

    # List of sick people is reset
    theSick = []
    maxRecTime = 0
    avgRec = 0
    # Looping through people to change values
    for person in people:
        # average / max recovery time
        if person.getRecovery() > maxRecTime:
            maxRecTime = person.getRecovery()
        avgRec += person.getRecovery()
        # If they have recovered they are immmune and not sick
        if person.getRecovery() <= 0:
            person.setImmune(True)
            person.setSick(False)
        # If they're immune I add 1 to the number of immune people
        if person.isImmune():
            immuneNum += 1
        # Added to sick list if they're sick
        if person.isSick():
            theSick.append(person)
    # changing the highest number of sick people throughout the simulation
    if len(theSick) > mostSick:
        mostSick = len(theSick)
    avgRec /= numPeople
    day += 1
    # Adding info to the lists to plot it later
    days.append(day)
    listSickNum.append(len(theSick))
    listImmuneNum.append(immuneNum)
    # printing the info to the console
    print('day %d\nsick %d\nimmune %d\nlongest recovery time %d\naverage recovery time %d\n' % (day, len(theSick), immuneNum, maxRecTime, avgRec))

avgPeopleSpread = 0
for person in people:
    if person.isImmune():
        avgPeopleSpread += person.getNumSpread()
avgPeopleSpread /= immuneNum
# printing statistics
print("The average recovery time is: %d days" %avgRecovery)
print("The average number of transmissions per infection was %0.1f people" %avgPeopleSpread)
print("The percent of the population that became infected was: %0.3f%c" % (100*immuneNum/numPeople, '%'))
print("The maximum number of the population that became infected was %d people" %mostSick)
print("The infection died out in %d days" %len(days))
# plotting the data
plt.plot(days,listSickNum)
plt.plot(days,listImmuneNum)
plt.legend(['Number of Sick People', 'Number of Immune People'])
plt.xlabel('day number')
plt.ylabel('number of sick people')
plt.title('Day number VS. Number of sick people')
plt.show()