from ContactTracer import ContactTracer

OurTracer = ContactTracer()


class User:
    '''Each user stores their recent interactions and their infection
    level: Healthy, Potentially Infected, or Infected
    
    User handles user-end functions such as logging interactions and
    reporting symptoms'''

    def __init__(self, name):
        '''name is a string representing the user's name'''
        self.name = name
        self.status = 'Healthy'
        #For space purposes, only track interactions over the past week
        self.interactions = [[]]*7
        self.group = OurTracer

    def __repr__(self):
        return self.name + ': ' + str(self.totalInteractions()) + ' with ' + str(self.uniqueInteractions()) + ' different people\n'


    def totalInteractions(self):
        return sum(len(x) for x in self.interactions)

    def uniqueInteractions(self):
        uniquePeople = []
        for day in self.interactions:
            for person in day:
                if person not in uniquePeople:
                    uniquePeople += [person]
        return len(uniquePeople)
