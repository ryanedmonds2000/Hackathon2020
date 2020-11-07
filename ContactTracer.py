from User import User

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
        output = 'Today is ' + str(self.day) + ".\n There are currently " + str(len(self.userList)) + " users:\n\n"
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