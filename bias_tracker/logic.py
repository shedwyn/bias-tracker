"""functions and data for rendering views"""

from bias_tracker.models import Descriptor
from bias_tracker.models import Person
# from bias_tracker.models import User
from bias_tracker.models import Incident

# from . import views

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
    """take in id, return number of incidents logged as author by id"""
    total_incidents_as_author = \
        Incident.objects.filter(author__exact=user_id).count()
    return total_incidents_as_author


def get_percent_exclusion_logged_as_author(user_id):
    """take in User.id and return incident percent for exclusionary"""
    total_incidents_as_author = get_total_incidents_as_author(user_id)
    count_exclusive_as_author = Incident.objects.filter(
        author__exact=user_id, incident_type__exact='Exclusion'
    ).count()
    percent = round(
        (count_exclusive_as_author / total_incidents_as_author) * 100, 1
    )
    return percent


def get_percent_inclusion_logged_as_author(user_id):
    """take in User.id and return incident percent for inclusionary"""
    total_incidents_as_author = get_total_incidents_as_author(user_id)
    count_inclusion_as_author = Incident.objects.filter(
        author__exact=user_id, incident_type__exact='Inclusion'
    ).count()
    percent = round(
        (count_inclusion_as_author / total_incidents_as_author) * 100, 1
    )
    return percent


def count_descriptors_for_author(incidents_as_author):
    """take Incidents, count all Incident references to descriptor & return"""
    descriptor_counts = {}
    for incident in incidents_as_author:
        descriptors = incident.descriptors.all()
        for descriptor in descriptors:
            if descriptor.descriptor not in descriptor_counts:
                descriptor_counts[descriptor.descriptor] = 1
            else:
                descriptor_counts[descriptor.descriptor] += 1
    return descriptor_counts


def get_descriptor_counts_as_author(user_id):
    """take User.id, return dict of descriptors with count"""
    incidents_as_author = Incident.objects.filter(author__exact=user_id)
    descriptor_counts = count_descriptors_for_author(incidents_as_author)
    descriptors_and_counts = descriptor_counts.items()
    return descriptors_and_counts


def get_total_incidents_as_subject(subject_id):
    """take in id, return number of incidents logged as subject for id"""
    total_incidents_as_subject = \
        Incident.objects.filter(subjects__exact=subject_id).count()
    return total_incidents_as_subject


def get_percent_exclusion_logged_as_subject(subject_id):
    """take in id and return incident percent for exclusionary"""
    total_incidents_as_subject = get_total_incidents_as_subject(subject_id)
    count_exclusive_as_subject = Incident.objects.filter(
        subjects__exact=subject_id, incident_type__exact='Exclusion'
    ).count()
    percent = round(
        (count_exclusive_as_subject / total_incidents_as_subject) * 100, 1
    )
    return percent


def get_percent_inclusion_logged_as_subject(subject_id):
    """take in id and return incident percent for inclusionary"""
    total_incidents_as_subject = get_total_incidents_as_subject(subject_id)
    count_inclusive_as_subject = Incident.objects.filter(
        subjects__exact=subject_id, incident_type__exact='Inclusion'
    ).count()
    percent = round(
        (count_inclusive_as_subject / total_incidents_as_subject) * 100, 1
    )
    return percent


def count_descriptors_for_subject(incidents_as_subject):
    """take Incidents, count all Incident references to descriptor & return"""
    descriptor_counts = {}
    for incident in incidents_as_subject:
        descriptors = incident.descriptors.all()
        for descriptor in descriptors:
            if descriptor.descriptor not in descriptor_counts:
                descriptor_counts[descriptor.descriptor] = 1
            else:
                descriptor_counts[descriptor.descriptor] += 1
    return descriptor_counts


def get_descriptor_counts_as_subject(subject_id):
    """take id, return dict of descriptors with count"""
    incidents_as_subject = Incident.objects.filter(subjects__exact=subject_id)
    descriptor_counts = count_descriptors_for_subject(incidents_as_subject)
    descriptors_and_counts = descriptor_counts.items()
    return descriptors_and_counts


def create_descriptor_and_count_dicts(subject_id):
    """take in tuple pair, return list of dictionaries with 2 key:val pairs"""
    descriptors_and_counts = get_descriptor_counts_as_subject(subject_id)
    descriptor_and_count_dicts = []
    for i in descriptors_and_counts:
        dict_item = {'descriptor': i[0], 'count': i[1]}
        descriptor_and_count_dicts.append(dict_item)
    return descriptor_and_count_dicts


def create_incident_type_list(incident_types):
    """take in tuple pairs and return single list of two items"""
    incident_type_choices = []
    for item in incident_types:
        incident_type_choices.append(item[0])
    return incident_type_choices


def log_new_incident(author, subjects, incident_type, descriptors):
    """take in incident fields and instantiate new incident"""
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
        # do I need the above or can I just put "descriptor" in below?
        new_incident.descriptors.add(desc_id)
    return 'New Incident Submitted'


def create_json_object(subject_id):
    """take in id, create items for JSON dict, make JSON dict"""
    inclusion_percent = get_percent_inclusion_logged_as_subject(subject_id)
    print('INCLUSION', inclusion_percent)
    exclusion_percent = get_percent_exclusion_logged_as_subject(subject_id)
    print('EXCLUSION', exclusion_percent)
    print('**********************************')
    descriptor_counts = create_descriptor_and_count_dicts(subject_id)
    print('DESCRIPTOR', descriptor_counts)
    print('**********************************')
    print('**********************************')
    print('**********************************')
    json_object = {
        'inclusion': inclusion_percent,
        'exclusion': exclusion_percent,
        'descriptors': descriptor_counts
    }
    print('**********************************')
    # print(json_object)
    return json_object
