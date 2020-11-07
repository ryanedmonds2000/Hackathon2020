from User import User

class ContactTracer:
    '''ContactTracer will keep a list of every person currently using the tracer, and is responsible
    for allowing different users to communicate with eachother
    
    ContactTracer handles back-end functions such as updating traces and
    the progression of time'''

    def __init__(self):
        self.userList = []      #list containing every registered person
        self.day = 0            #calendar currently only tracks number of days

    def __repr__(self):
        output = 'Today is ' + str(self.day) + ".\n There are currently " + str(size(self.userList)) + " users:\n\n"
        for user in self.userList:
            output += repr(user) + '\n\n'
        return output

