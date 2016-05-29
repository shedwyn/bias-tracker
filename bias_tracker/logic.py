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
    # is this necessary?
    incident_type_choices = create_incident_type_list(incident_types)
    return incident_type_choices


def get_total_incidents_as_author(user_id):
    """take in name, return number of incidents logged by name"""
    total_incidents_as_author = \
        Incident.objects.filter(author__exact=user_id).count()
    return total_incidents_as_author


def get_percent_exclusion_logged_as_author(user_id):
    """take in User.id and return incident percent for exclusionary"""
    total_incidents_as_author = get_total_incidents_as_author(user_id)
    count_exclusive_as_author = Incident.objects.filter(
        author__exact=user_id, incident_type__exact='Exclusion'
    ).count()
    percent = (count_exclusive_as_author / total_incidents_as_author) * 100
    return percent


def get_percent_inclusion_logged_as_author(user_id):
    """take in User.id and return incident percent for inclusionary"""
    total_incidents_as_author = get_total_incidents_as_author(user_id)
    count_inclusion_as_author = Incident.objects.filter(
        author__exact=user_id, incident_type__exact='Inclusion'
    ).count()
    percent = (count_inclusion_as_author / total_incidents_as_author) * 100
    return percent


def get_descriptor_counts_as_author(user_id):
    """take User.id, return dict of descriptors with count"""
    incidents_as_author = Incident.objects.filter(author__exact=user_id)
    descriptor_counts = {}
    for incident in incidents_as_author:
        descriptors = incident.descriptors.all()
        for descriptor in descriptors:
            if descriptor not in descriptor_counts:
                descriptor_counts[descriptor] = 1
            else:
                descriptor_counts[descriptor] += 1
    print(descriptor_counts)
    return descriptor_counts


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
