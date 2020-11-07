from ContactTracer import ContactTracer

OurTracer = ContactTracer()


class User:
    '''Each user stores their recent interactions and their infection
    level: Healthy, Potentially Infected, or Infected
    
    User handles user-end functions such as logging interactions and
    reporting symptoms'''

    def __init__(self, name):
        '''
        name is a string representing the user's name

        Users are expected to register when healthy, and should immediately
        declare symptoms if not
        '''
        self.name = name
        self.status = 'Healthy'
        #For space purposes, only track interactions over the past week
        #Day of the week represented in modulo 7
        self.interactions = [[]]*7
        self.group = OurTracer
        #potentialInfectionDay exists so that potentiall infected users
        #can eventually be cleared
        self.potentialInfectionDay = 0
        #infectionGeneration indicates how "far" the user is from an infected individual
        #the higher the number, the lower the chance of an infection
        self.infectionGeneration = 0

    def __repr__(self):
        '''
        TODO: custom descriptions for potentially infected individuals depending on the generation?
        '''
        return self.name + 'is currently ' + self.status + ':\n They have had' + str(self.totalInteractions()) + ' with ' + str(self.uniqueInteractions()) + ' different people.'


    def totalInteractions(self):
        return sum(len(x) for x in self.interactions)

    def uniqueInteractions(self):
        uniquePeople = []
        for day in self.interactions:
            for person in day:
                if person not in uniquePeople:
                    uniquePeople += [person]
        return len(uniquePeople)

    def interact(self, users):
        """
        TODO:
        users should be a list of other Users
        for each member of users list, add them to self's interactions
        for the current day, and vice versa
        """
        pass

    def reportSymptoms(self):
        """
        TODO:
        Update the user to being Infected, and trace their recent interactions
        """
        pass