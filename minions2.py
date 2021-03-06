class Minion:
    """ A minion, with a name. """

    # a class variable, counting the number of minions
    population = 0

    def __init__(self, name):
        """ Initialize the minion """
        self.name = name
        print('Minion {} is formed'.format(self.name))

        Minion.population += 1

    def __repr__(self):
        """ Representation of minion """
        return '<A minion named {}>'.format(self.name)

    def __str__(self):
        """ Printable minion """
        return 'Hi! My master calls me {}'.format(self.name)

    def dismiss(self):
        """ Dismiss me """
        print('{} is dismissed!'.format(self.name))

        Minion.population -= 1
        if Minion.population == 0:
            print('{} was the last minion.'.format(self.name))
        else:
            print('There are still {:d} minions available'
                  .format(Minion.population))

    def say_hi(self):
        """ Let the minion introduce itself """
        print(self)

    @classmethod
    def how_many(cls):
        """ Prints the current population """
        print('We have {:d} minions'.format(cls.population))
