from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class CandidateProfile(User):

    gender_choice = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )

    age_choice = (
        ('16-20', '16-20'),
        ('21-30', '21-30'),
        ('31-40', '31-40'),
        ('40+', '40+'),
    )

    gender = models.CharField(max_length=20, choices=gender_choice)
    age = models.CharField(max_length=20, choices=age_choice)
    location = models.CharField(max_length=200, default='London')
    phone_number = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    note = models.TextField(max_length=500,
                            blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('profile-detail', args=[str(self.id)])


