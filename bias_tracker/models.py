"""bias_tracker Models configuration"""

from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    """name of Subject for recorded Incident"""

    name = models.CharField(max_length=40)

    def __str__(self):
        """docstring"""
        return 'Person_str({}, {})'.format(self.id, self.name)

    def __repr__(self):
        """docstring"""
        return 'Person_repr({!r}, {!r})'.format(self.id, self.name)


class Descriptor(models.Model):
    """quick one-line tags for subject behavior during Incident"""

    descriptor = models.CharField(
        'Incident Type Descriptor(s)',
        max_length=100
    )

    def __str__(self):
        """docstring"""
        return 'Descriptor_str({}, {})'.format(self.id, self.descriptor)

    def __repr__(self):
        """docstring"""
        return 'Descriptor_repr({!r}, {!r})'.format(self.id, self.descriptor)


class Incident(models.Model):
    """collection of all details for incident.

    links to models User, Person and Descriptor
    """

    DEFAULT_DESCRIPTION = 'describe incident detail here'
    default_date = '2016-01-01'
    TYPE_CHOICES = (
        ('Exclusion', 'Exclusion'),
        ('Inclusion', 'Inclusion')
    )
    # look into pre-delete and filling incidents with sub_id 1
    author = models.ForeignKey(User)
    subjects = models.ManyToManyField(Person, default=1)
    # Filing date is the auto-add date author creates incident
    filing_date = models.DateTimeField(auto_now_add=True)
    # Incident date is specifically the date the Incident happened
    incident_date = models.DateField(default=default_date)
    incident_time = models.TimeField(blank=True)
    incident_type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    descriptors = models.ManyToManyField(Descriptor, default=1)
    text_description = models.TextField(
        'Incident Description',
        default=DEFAULT_DESCRIPTION,
    )

    def __str__(self):
        """docstring"""
        return 'Incident_str({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
            self.id,
            self.author,
            self.filing_date,
            self.incident_date,
            self.incident_time,
            self.subjects.all(),
            self.incident_type,
            self.descriptors.all(),
            self.text_description
        )

    def __repr__(self):
        """docstring"""
        return 'Incident_repr(\
            {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}\
        )'.format(
            self.id,
            self.author,
            self.filing_date,
            self.incident_date,
            self.incident_time,
            self.subjects.all(),
            self.incident_type,
            self.descriptors.all(),
            self.text_description
        )
