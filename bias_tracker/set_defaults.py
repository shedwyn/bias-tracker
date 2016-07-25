"""functions to instantiate default values for both Person and Descriptor
classes
"""

from bias_tracker.models import Descriptor
from bias_tracker.models import Person


DEFAULT_PERSONS = ['Organization', 'Individual']

GENDER_BIAS_DEFAULT_DESCRIPTORS = [
    'Missing Descriptor', 'E-not listening',
    'E-not inviting/including in discussion/activity',
    'E-facial/hand/verbal expression of impatience/boredom',
    'E-scornful vocal tone', 'E-talking over', 'E-not responding to question',
    'E-bragging or pushing to compete', 'E-dismissing ideas without reason',
    'E-treating as invisible', 'E-over solicitation',
    'E-over simplified explanation', 'E-answering question not asked',
    'E-directed toward tasks deemed \'woman\'s work\'',
    'E-credit taken/not given', 'I-deliberately included in discussion',
    'I-credit given', 'I-listening', 'I-sharing talking space',
    'I-constructive criticism', 'I-open to ideas', 'I-willing to explain',
    'I-tailors explanation style/method', 'I-positive tonality/gestures',
    'I-invited to/willing to work together', 'I-good eye contact'
]

DEFAULT_DESCRIPTORS = ['Other']


def create_default_persons(list1):
    """instantiate Person Model (table) with default options"""
    for name in DEFAULT_PERSONS:
        new_person = Person(name=name)
        new_person.save()
    print('Person defaults have been set!')


def create_default_descriptors(big_list, small_list):
    """instantiate Descriptor Model (table) with default options"""
    default_choice = choose_which_defaults_to_use()
    if default_choice == 'YES':
        for descriptor in big_list:
            new_descriptor = Descriptor(descriptor=descriptor)
            new_descriptor.save()
        return 'Done!'
    else:
        for descriptor in small_list:
            new_descriptor = Descriptor(descriptor=descriptor)
            new_descriptor.save()
        return 'Done!'


def choose_which_defaults_to_use():
    """return user selection of default descriptor choices"""
    print(
        'Do you want to import just the full set of Gender-Bias descriptors?',
        '\n',
        'Type \'YES\' to import all descriptors (you can make changes in',
        ' Admin screen to further individualize your set)',
        'Type \'NO\' to import only the two (2) basic descriptors.'
    )
    yes_options = ['y', 'Y', 'Yes', 'YES', 'yes']
    no_options = ['n', 'N', 'No', 'NO', 'no']
    answer = input('Please answer YES or NO:   ')
    if answer in yes_options:
        return 'YES'
    elif answer in no_options:
        return 'NO'
    else:
        print('I did not understand your choice')
        choose_which_defaults_to_use()


def start_program_or_quit():
    """warn user of requirements to run this program and return answer"""
    print(
        'This program will instantiate the most basic items you need to start',
        ' logging incidents.  This program will only work if you have:',
        '1) Initialized Django',
        '2) Initialized a new database',
        '3) Run it from within the Django Python Shell',
    )
    begin_answer = input('Are you ready to proceed?')
    acceptable_answers = ['no', 'NO', 'No', 'n', 'N']
    if begin_answer in acceptable_answers:
        return False
    return True


def main():
    """run all listed functions in this module"""
    if start_program_or_quit() is True:
        print('starting Person load...')
        create_default_persons(DEFAULT_PERSONS)
        print('finished Person load, starting Descriptor load...')
        create_default_descriptors(
            GENDER_BIAS_DEFAULT_DESCRIPTORS,
            DEFAULT_DESCRIPTORS
        )
    print('Finished!')
    return

if __name__ == '__main__':
    main()
