
class ContactTracer:
    '''ContactTracer will keep a list of every person currently using the tracer, and is responsible
    for allowing different users to communicate with eachother
    
    ContactTracer handles back-end functions such as updating traces and
    the progression of time'''

    def __init__(self):
        '''
        TODO: could eventually incorporate actual calendar system?
        '''
        self.userList = []        #list containing every registered person
        self.day = 0              #calendar currently only tracks number of days
        self.incubationPeriod = 3 #If symptoms are reported, trace all contacts from up to this number of days in the past
                                  #Must be between 0 and 6
        self.lifespan =  7        #If user goes this long without reporting systems, can go back to being healthy

    def __repr__(self):
        output = 'Today is the day' + str(self.day) + ".\nThere are currently " + str(len(self.userList)) + " users:\n\n"
        for user in self.userList:
            output += repr(user) + '\n\n'
        return output




    def traceInteractions(self, user, days):
        """
        TODO:
        traceInteractions will take in an Infected or Potentially Infected
        user "user", and will track all interactions made by said user within
        the given amount of time. For each other person found, update them to be
        Potentially Infected and recursively track their interactions

        Potential issue: since we only operate one day at a time, some people
        will be falsely tagged due to interactions happening at different times
        of day
        """
        pass

    def newDay(self):
        """
        TODO:
        increment self.day by 1

        make space in each user's interactions list for a new day of interactions

        for any users currently or potentially infected, trace their interactions for that day

        for any potentially infected users who were last potentially infected
        longer ago than self.lifespan, set to Healthy
        """
        pass

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
        OurTracer.userList += [self]



    def __repr__(self):
        '''
        TODO: custom descriptions for potentially infected individuals depending on the generation?
        '''
        return self.name + ' is currently ' + self.status + ':\n They have had ' + str(self.totalInteractions()) + ' interactions with ' + str(self.uniqueInteractions()) + ' different people.'


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