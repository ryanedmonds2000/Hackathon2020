# Hackathon2020

Ryan Edmonds

Collins Kariuki

Amber Hughes


FUNCTIONALITY:

ContactTracer currently allows for users to log their interactions with other users by date and time, and will retroactively trace interactions whenever a user reports that they are experiencing symptoms. Each user has a list of lists of interactions logged in the past week, which can be observed to determine a network of interactions.

HOW TO USE:

Upon running ContactTracer, the OurTracer object will be created. Possible user-end functions include:
User = User("name") - creates a new user with the given name, and adds them to the contact tracing list.
User.interact([user],time) - allows for a user to report interactions with other users at a given time.
User.reportSymptoms() - allows for a user to report if they are infected.
User.reportHealthy() - allows for a user to report if they have recovered from their infection.
OurTracer.newDay() - progresses the calendar to the next day, tracking any relevant interactions from that day.

print(OurTracer) prints the current day, the current number of users, and then for each user, prints their health status and how many interactions they have had with how many different people in 7 days.
