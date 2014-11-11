# Appliance.py
# Course: Programmeertheorie 2014
# Case: Kaartkleuren
# Group: Kleurenblind
# Members: John, Thijs, Sofia
# November 2014, Amsterdam

import csv

#Instantiate object that defines country/province
class Country(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
# open connections text file
user1 = []
connections1 = []
user2 = []
connections2 = []
user3 = []
connections3 = []

with open('socialconnections.csv','rb') as csvfile:
    connections = csv.reader(csvfile, delimiter=';')  
    # reads file         
    for row in connections:
        user1.append(row[0])
        connections1.append(row[1])
        if row[0] == 'Netwerk#2':
            break
    for row in connections:
        user2.append(row[0])
        connections2.append(row[1]) 
        if row[0] == 'Netwerk #3':
            break
    for row in connections:
        user3.append(row[0])
        connections3.append(row[1])                     
        
# put data in dictionaries
netwerk1 = dict(zip(user1, connections1))
netwerk2 = dict(zip(user2, connections2))
netwerk3 = dict(zip(user3, connections2))

#netwerk1[user1] = connections1
#netwerk2[user2] = connections2
#netwerk3[user3] = connections3

print netwerk1
print netwerk2
print netwerk3

        
def ConnectedTo(country):
    '''
    This function returns a list of adjecent countries.
    
    @param country: the name of the country
    '''
    # Needs to be implemented
    return country_list

def AssignColor(country, country_list):
    '''
    This function checks which color the adjecent countries have and returns the first non used color.

    @param country: the name of the country
    @param country_list: ist of adjecent countries
    '''
    # Needs to be implemented.
    
    return color
    
    
