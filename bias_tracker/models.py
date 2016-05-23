from django.db import models


class Author(models.Model):
    """name of Author for recorded Incident"""
    name = models.CharField(max_length=40)

    def __str__(self):
        return 'Author_str({}, {})'.format(self.id, self.name)

    def __repr__(self):
        return 'Author_repr({}, {})'.format(self.id, self.name)


class Subject(models.Model):
    """name of Subject for recorded Incident"""
    name = models.CharField(max_length=40)

    def __str__(self):
        return 'Subject_str({}, {})'.format(self.id, self.name)

    def __repr__(self):
        return 'Subject_repr({}, {})'.format(self.id, self.name)


class Descriptor(models.Model):
    """quick one-line tags for specific details of the Incident"""
    descriptor = models.CharField(
        'incident type descriptor(s)',
        max_length=100
    )

    def __str__(self):
        return 'Descriptor_str({}, {})'.format(self.id, self.descriptor)

    def __repr__(self):
        return 'Descriptor_repr({}, {})'.format(self.id, self.descriptor)


class Incident(models.Model):
    """primary class for incident recording.  'i_' used as abbreviation for
    'incident'."""
    # foreing and manytomany need default keys so on_delete can be changed
    author_id = models.ForeignKey(Author,)  # should match login
    # how can I do multiple iSubjects for the iSubject field?
    i_subject_id = models.ManyToManyField(
        Subject,
        verbose_name='incident subject(s)'
    )  # list of persons
    filing_date = models.DateTimeField()
    i_date = models.DateField('incident date')
    i_time = models.TimeField('incident time')
    i_type = models.CharField('incident type', max_length=3)
    # does on_delete delete the ForeignKey or all data?
    i_descriptors = models.ManyToManyField(
        Descriptor,
        verbose_name='incident type descriptor(s)'
    )
    text_description = models.TextField('incident description')

    def __str__(self):
        return 'Incident_str({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
            self.id, self.author_id, self.i_subject_id, self.filing_date,
            self.i_date, self.i_time, self.i_type, self.i_descriptors,
            self.text_description
        )

    def __repr__(self):
        return 'Incident_repr({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
            self.id, self.author_id, self.i_subject_id, self.filing_date,
            self.i_date, self.i_time, self.i_type, self.i_descriptors,
            self.text_description
        )
