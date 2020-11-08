
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
        output = 'Today is day ' + str(self.day) + ".\nThere are currently " + str(len(self.userList)) + " users:\n\n"
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
        """
        #first set all users the first user interacted with to have status potentially infected
        #person[0] is the person, person[1] is the time
        while days >= 0:
            for person in user.interactions[(self.day - days) % 7]:
                if person[0].status == "Healthy" and user.potentialInfectionTime <= person[1]:
                    person[0].potentialInfectionDay = self.day - days
                    person[0].potentialInfectionTime = person[1]
                    person[0].status="Potentially Infected"
                    self.traceInteractions(person[0],days)
            days -= 1

    def newDay(self):
        """creates a new day; continue tracking people with positive test on day by day basis """
        #TODO:
        #increment self.day by 1
        
        #make space in each user's interactions list for a new day of interactions
        for user in self.userList:
            user.interactions[(self.day + 1) % 7] = []
        #for any users currently or potentially infected, trace their interactions for that day
            if user.status=="Infected" or user.status=="Potentially Infected":
                if user.potentialInfectionDay != self.day:
                    user.potentialInfectionTime = 0
                    self.traceInteractions(user, 0)
        #for any potentially infected users who were last potentially infected longer ago than self.lifespan, set to Healthy
            if user.status == "Potentially Infected" and self.day - user.potentialInfectionDay > self.lifespan:
                user.status="Healthy"
        self.day+=1
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
        self.interactions = [[],[],[],[],[],[],[]]
        self.group = OurTracer
        #potentialInfectionDay exists so that potentiall infected users
        #can eventually be cleared
        self.potentialInfectionDay = 0
        self.potentialInfectionTime = 0
        #infectionGeneration indicates how "far" the user is from an infected individual
        #the higher the number, the lower the chance of an infection
        self.infectionGeneration = 0
        self.group.userList += [self]



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
                if person[0] not in uniquePeople:
                    uniquePeople += [person[0]]
        return len(uniquePeople)

    def interact(self, users, time):
        """
        TODO:
        users should be a list of other Users
        for each member of users list, add them to self's interactions
        for the current day, and vice versa
        time is when they interacted (military time)
        """
        for user in users:
            self.interactions[self.group.day % 7] += [(user,time)]
            user.interactions[self.group.day % 7] += [(self,time)]

    def reportSymptoms(self):
        """
        # Update the user to being Infected, and trace their recent interactions
        """
        self.status="Infected"
        self.infectionGeneration = 1
        self.potentialInfectionTime = 0
        self.potentialInfectionDay = self.group.day - self.group.incubationPeriod
        self.group.traceInteractions(self, self.group.incubationPeriod)

    def reportHealthy(self):
        """
        Update the user to being healthy
        """
        self.status="Healthy"