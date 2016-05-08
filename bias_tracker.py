class Person:
    """name of person assigned to unique ID"""
    def __init__(self, name, gender, minority_status):
        self.name = name
        self.gender = gender
        self.minority_status = minority_status


class Incident:
    """primary class for incident recording.  'i_' used as abbreviation for
    'incident'."""
    def __init__(
        self, author_id, type_id, i_subject_id, filing_date, i_date, i_time,
        i_type, type_descriptors, subject_matter, subject_matter_strayed,
        description, problem_solving_during, problem_solving_after,
        physical_location, situation_group_size, situation_group_leader
    ):
        self.author_id = author_id
        self.i_subject_id = i_subject_id  # list of persons about whom incident
        # is being recorded
        self.filing_date = filing_date
        self.i_date = i_date
        self.i_time = i_time
        self.i_type = i_type  # pos or negative
        self.type_descriptors = type_descriptors  # list
        self.i_intended_subject_matter = i_intended_subject_matter
        self.subject_matter_strayed = subject_matter_strayed
        self.i_description = i_description
        self.problem_solving_during = problem_solving_during
        self.problem_solving_after = problem_solving_after
        self.physical_location = physical_location
        self.situation_group_size = situation_group_size
        self.situation_group_leader = situation_group_leader


#


def main():
    # collection of functions
    pass

if __name__ == '__main__':
    main()
