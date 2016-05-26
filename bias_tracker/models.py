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
    """quick one-line tags for specific details of the Incident"""

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

    'i_' used as abbreviation for 'incident'.
    """

    TYPE_CHOICES = (
        ('Exclusion', 'Exclusion'),
        ('Inclusion', 'Inclusion')
    )
    # foreing and manytomany need default keys so on_delete can be changed
    author = models.ForeignKey(User)
    subjects = models.ManyToManyField(Person)  # list of persons
    # filing_date = models.DateTimeField('Filing Date')
    # i_date = models.DateField('Incident Date')
    # i_time = models.TimeField('Incident Time', blank=True)
    incident_type = models.CharField(
        'Incident Type',
        choices=TYPE_CHOICES,
        max_length=10
    )
    descriptors = models.ManyToManyField(Descriptor)
    # text_description = models.TextField('Incident Description')

    def __str__(self):
        """docstring"""
        return 'Incident_str({}, {}, {}, {}, {})'.format(
            self.id,
            self.author,
            self.subjects.all(),
            self.incident_type,
            self.descriptors.all()
        )
        # self.filing_date, self.i_date, self.i_time, self.text_description

    def __repr__(self):
        """docstring"""
        return 'Incident_repr({!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.id,
            self.author,
            self.subjects.all(),
            self.incident_type,
            self.descriptors.all()
        )
