"""Birthday Paradox Simulation, by Attabeezy
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-projects
Tags: short, math, simulation"""

import datetime
import random


def get_birthday(number_of_birthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        start_of_year = datetime.date(2001, 1, 1)
        
        #Get a random day into the year:
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays
