"""functions and data for rendering views"""

from bias_tracker.models import Descriptor
from bias_tracker.models import Person
from bias_tracker.models import User
from bias_tracker.models import Incident

from . import views

# 'Incident_str({}, {}, {}, {}, {})'.format(
#     self.id, self.author, self.subjects, self.incident_type, self.descriptors


def grab_subject_options():
    """grab incident subject choices for page"""
    return Person.objects.all()


def grab_descriptor_options():
    """grab incident descriptor choices for page"""
    return Descriptor.objects.all()


def grab_type_options():
    """grab incident type choices for page"""
    return Incident.TYPE_CHOICES
#
#
# def generate_error_message():
#     pass
#
#



# MENU PAGE #
#


# INCIDENT PAGE #
