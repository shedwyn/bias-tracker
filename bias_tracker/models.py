"""bias_tracker Models configuration"""

from django.db import models


class Person(models.Model):
    """name of Author for recorded Incident"""

    name = models.CharField(max_length=40, default='default_name')

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

    #  Is the set default on Foreign supposed to be in the other class?
    # def call_person_default():
    #     """calls the Person default value"""
    #     return Person.default_name
    #
    # def call_descriptor_default():
    #     """calls the Descriptor default value"""
    #     return Descriptor.default_val

    TYPE_CHOICES = (
        ('Exclusion', 'Exclusion'),
        ('Inclusion', 'Inclusion')
    )
    # foreing and manytomany need default keys so on_delete can be changed
    author = models.ForeignKey(
        Person,
        related_name='incident_as_subjects',
        # on_delete=models.SET_DEFAULT,
        # default=call_person_default
    )
    # should match login
    subjects = models.ManyToManyField(
        Person,
        related_name='incidents_as_author',
        # on_delete=models.SET_DEFAULT,
        # default=call_person_default,

    )  # list of persons
    filing_date = models.DateTimeField('Filing Date')
    i_date = models.DateField('Incident Date')
    i_time = models.TimeField('Incident Time', blank=True)
    i_type = models.CharField(
        'Incident Type',
        choices=TYPE_CHOICES,
        max_length=10
    )
    i_descriptors = models.ManyToManyField(
        Descriptor,
        # on_delete=models.SET_DEFAULT,
        verbose_name='Descriptors of Incident Type',
        # default=call_descriptor_default
    )
    text_description = models.TextField('Incident Description')

    def __str__(self):
        """docstring"""
        return 'Incident_str({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
            self.id, self.author, self.subjects.all(), self.filing_date,
            self.i_date, self.i_time, self.i_type, self.i_descriptors.all(),
            self.text_description
        )

    def __repr__(self):
        """docstring"""
        return 'Incident_repr({!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.id, self.author, self.subjects.all(), self.filing_date,
            self.i_date, self.i_time, self.i_type, self.i_descriptors.all(),
            self.text_description
        )
