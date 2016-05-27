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
    incident_types = Incident.TYPE_CHOICES
    incident_type_choices = create_incident_type_list(incident_types)
    return incident_type_choices


def create_incident_type_list(incident_types):
    """take in tuple pairs and return single list of two items"""
    incident_type_choices = []
    for item in incident_types:
        incident_type_choices.append(item[0])
    return incident_type_choices


def log_new_incident(author, subjects, incident_type, descriptors):
    """take in incident fields and instantiate new incident"""
    print(author, subjects, incident_type, descriptors)
    new_incident = Incident(
        author=author,
        incident_type=incident_type,
    )
    new_incident.save()
    for subject in subjects:
        sub_id = int(subject)
        new_incident.subjects.add(sub_id)
    for descriptor in descriptors:
        desc_id = int(descriptor)
        new_incident.descriptors.add(descriptor)
    return 'New Incident Submitted'
