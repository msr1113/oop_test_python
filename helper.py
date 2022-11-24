

class Item:
    @staticmethod
    def is_integer():
        '''this should do something that has a relationship with the class but not something
        that must be unique per instance!
        '''

    @classmethod
    def instantiate_from_something(cls):
        '''
        this should alsp do something that has relationship with the class but usually those are
        used to manipulate different structures of data to instantiate objects,like we have done
        with csv
        '''

    item1 = Item()
    item1.is_integer(5)
    item1.instantiate_from_something()

