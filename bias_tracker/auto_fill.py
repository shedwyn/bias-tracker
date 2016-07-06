"""
Instantiate Bias_Tracker Person and Descriptor Models with minimum necessary
objects to function for new user.
"""


from bias_tracker.models.py import Person
from bias_tracker.models.py import Descriptor

AUTO_DESCRIPTORS = [
    'E - not listening',
    'E - not inviting/including in discussion/activity',
    'E - facial/hand/verbal expression of impatience/boredom',
    'E - scornful vocal tone',
    'E - talking over',
    'E - not responding tquestion',
    'E - bragging or pushing to compete',
    'E - dismissing ideas without reason',
    'E - treating as invisible',
    'E - over solicitation',
    'E - over simplified explanation',
    'E - answering question not asked',
    "E - directed toward tasks deemed women's work",
    'E - credit taken/not given',
    'I - deliberately included in discussion',
    'I - credit given',
    'I - listening',
    'I - sharing talking space',
    'I - constructive criticism',
    'I - open to ideas',
    'I - willing to explain',
    'I - tailors explanation style/method',
    'I - positive tonality/gestures',
    'I - critical thinking',
    'I - good eye contact',
    'I - intervened in incidence of bias',
    'I - asked for information/assistance'
]

AUTO_PERSON = [
    'Organization',
    'Individual'
]


def auto_instantiate_descriptors():
    for i in AUTO_DESCRIPTORS:
        
