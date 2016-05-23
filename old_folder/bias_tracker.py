class Person:
    """name of person assigned to unique ID"""
    def __init__(self, name):
        self.name = name
        # self.gender = gender # these belong to advanced version
        # self.minority_status = minority_status # these belong to adv version


class Incident:
    """primary class for incident recording.  'i_' used as abbreviation for
    'incident'."""
    def __init__(
        self, author_id, i_subject_id, filing_date, i_date, i_time,
        i_type, type_descriptors, description
    ):
        self.author_id = author_id
        self.i_subject_id = i_subject_id  # list of persons about whom incident
        # is being recorded
        self.filing_date = filing_date
        self.i_date = i_date
        self.i_time = i_time
        self.i_type = i_type  # pos or negative
        self.type_descriptors = type_descriptors  # list
        self.i_description = i_description


class Descriptor:
    """descriptor 'tag' which will be critical part of graphical result
    output"""
    def __init__(self, descriptor):
        self.descriptor = descriptor


user_request = input_item  # get input from django as to which report user//
# wants to run, use this as argument to trigger a function that calls //
# the function that contains the functions related to that particular report.

# Take in list of descriptors, sort, count
# Take in self.i_type where author_id matches, split pos to neg, count //
# tally
# Take in self.i_type where i_subject_id matches request, split pos to neg, //
# count, tally


def main():
    # collection of functions
    pass

if __name__ == '__main__':
    main()
