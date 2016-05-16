# from . import bias_tracker

# class Person:
#     """name of person assigned to unique ID"""
#     def __init__(self, name):
#         self.name = name


# LOGIN PAGE #
def testing_write_methods():
    """just testing if i can write to csv file"""
    human_database = {
        'erin': ("Snow White", 'F'),
        'grumpy': ('Grumpy Dwarf', 'M'),
        # 'sneezy': 'Sneezy Dwarf', 'M',
        # 'bashful': 'Bashful Dwarf', 'M'
    }
    with open('database.txt', 'w') as humans_db_file:
        for name, details in human_database.items():
            line = '{} {}\n'.format(name, details)
            humans_db_file.write(line)


def write_more(key, values):
    with open(database.txt, 'w') as humans_db_file:
        human_database = humans_db_file.readlines()
    print(human_database)
    human_database.write(key values)
    print(human_database)


# MENU PAGE #




# INCIDENT PAGE #

write_more()
